import multiprocessing as mp
from multiprocessing.synchronize import Lock
from IpcSharedData import PubSubManager, SubscribersPipeConnections
from Publishers import MotionDetectorPub
from PubSubs import SingleShotDetectorPubSub
from Subscribers import LoggerSub
from Messages import MotionVectorMessage
from Topics import MotionVectorTopic, DetectionVectorTopic, TOPIC_BUILDER
from Topics.BaseTopic import BaseTopic
from ImageProcessors import DetectionProcessor


def detect_object(
        sub_senders: SubscribersPipeConnections,
        locker: Lock
) -> None:
    motion_topic = MotionVectorTopic(True, sub_senders)
    detection_topic = DetectionVectorTopic(True, sub_senders)
    single_shot = SingleShotDetectorPubSub()
    single_shot.subscribe(motion_topic)
    single_shot.add(detection_topic)
    detector = DetectionProcessor()
    while True:
        motion_msg = single_shot.get(motion_topic.name())
        locker.acquire()
        print("[DETECTION PROCESS] New motion msg: ", motion_msg)
        locker.release()
        detection_msg = detector.process(motion_msg)
        single_shot.publish(detection_msg)


def ipc_logging(
        sub_senders: SubscribersPipeConnections,
        locker: Lock
) -> None:
    sub_logger = LoggerSub()
    while True:
        for topic_name in sub_senders.keys():
            if (
                topic_name not in sub_logger.subscriptions()
                and topic_name in list(TOPIC_BUILDER.keys())
            ):
                topic_instance = TOPIC_BUILDER[topic_name](True, sub_senders)
                sub_logger.subscribe(topic_instance)
        for topic in BaseTopic.get_instances():
            locker.acquire()
            print("[LOGGING PROCESS] New msg: ", sub_logger.get(topic.name()))
            locker.release()


def detect_motion(
        sub_senders: SubscribersPipeConnections,
        locker: Lock
) -> None:
    message = MotionVectorMessage(
        1720246845, "Frame_1", 44, 55, 200, 200, [[2, 4], [3, 6]]
    )
    motion_vector = MotionVectorTopic(True, sub_senders)
    motion_detector = MotionDetectorPub()
    motion_detector.add(motion_vector)
    motion_detector.publish(message)


if __name__ == "__main__":
    lock = mp.Lock()
    with PubSubManager() as manager:
        subscribers_senders = manager.SubscribersPipeConnections()
        process_detection = mp.Process(
            target=detect_object,
            args=(
                subscribers_senders,
                lock,
            ),
        )
        process_detection.start()

        ipc_logger = mp.Process(
            target=ipc_logging,
            args=(
                subscribers_senders,
                lock,
            ),
        )
        ipc_logger.start()

        loop = True
        while loop:
            u_action = input()
            if u_action == "q":
                break

            process_motion = mp.Process(
                target=detect_motion,
                args=(
                    subscribers_senders,
                    lock,
                ),
            )
            process_motion.start()

            # DO OTHER STUFF...

            process_motion.join()
        process_detection.terminate()
        ipc_logger.terminate()
