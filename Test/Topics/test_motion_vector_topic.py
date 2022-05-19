from Topics import MotionVectorTopic
from IpcSharedData import SubscribersPipeConnections
from Messages import MotionVectorMessage
from Subscribers import LoggerSub
from Publishers import MotionDetectorPub
from typing import Callable


def test_get_instances():
    subs_pipe_conns = SubscribersPipeConnections()
    topic = MotionVectorTopic(subs_pipe_conns)
    assert isinstance(topic.get_instances(), list)


def test_name():
    subs_pipe_conns = SubscribersPipeConnections()
    topic = MotionVectorTopic(subs_pipe_conns)
    assert isinstance(topic.name(), str)


def test_publish_without_subscribers():
    subs_pipe_conns = SubscribersPipeConnections()
    topic = MotionVectorTopic(subs_pipe_conns)
    msg = MotionVectorMessage(
        1720246845, "Frame_1", 44, 55, 200, 200, [[2, 4], [3, 6]]
    )
    assert topic.publish(msg) is False


def test_publish_no_multiprocessing():
    motion_topic = MotionVectorTopic(multiprocessing=False)
    pub = MotionDetectorPub()
    pub.add(motion_topic)

    sub = LoggerSub()
    sub.subscribe(motion_topic)

    msgs = []

    counter = 3
    for i in range(counter):
        msgs.append(
            MotionVectorMessage(
                1720246840 + i, "Frame_1", 44, 55, 200, 200, [[2, 4], [3, 6]]
            )
        )
        pub.publish(msgs[i])

    for i in range(counter):
        gotten_msg = sub.get(motion_topic.name())
        assert isinstance(gotten_msg, MotionVectorMessage)
        assert str(msgs[i]) == str(gotten_msg)


# def subscribing(shared_pipe_conns):
#     sub_topic = MotionVectorTopic(shared_pipe_conns)
#     subscribers = 3
#     subs = []
#     for _ in range(subscribers):
#         subs.append(LoggerSub())
#         subs[-1].subscribe(sub_topic)
#     while True:
#         subs[-1].get(sub_topic.name())

# def test_publish_with_subscribers():
#     with PubSubManager() as manager:
#         subs_pipe_conns = manager.SubscribersPipeConnections()
#         topic = MotionVectorTopic(subs_pipe_conns)
#
#         process = mp.Process(target=subscribing, args=(subs_pipe_conns,))
#         process.start()
#         time.sleep(2)
#         assert topic.publish(MotionVectorMessage()) is True
#         time.sleep(2)
#         process.terminate()


def test_subscribe():
    subs_pipe_conns = SubscribersPipeConnections()
    topic = MotionVectorTopic(True, subs_pipe_conns)
    subscribers = 3
    for _ in range(subscribers):
        LoggerSub().subscribe(topic)

    assert len(topic._subscriptions) == subscribers
    for subscriber_callback in topic._subscriptions:
        assert isinstance(subscriber_callback, Callable)
