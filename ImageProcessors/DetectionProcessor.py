from .BaseProcessor import BaseProcessor
from Messages import BaseMessage, MotionVectorMessage, DetectionVectorMessage


class DetectionProcessor(BaseProcessor):
    """
    Detection processor class.
    Detects objects on images fed by a motion detector.
    """

    def __init__(self):
        super().__init__()

    def process(self, message: BaseMessage | None) -> DetectionVectorMessage:
        """Method which process the message.
        Detect objects from images fed by a motion detector. The motion
        detector publish messages of type MotionVectorMessage.

        Parameters
        ----------
        message: MotionVectorMessage
            Message to process must be of type MotionVectorMessage.

        Returns
        -------
        DetectionVectorMessage
            This process returns a message of type DetectionVectorMessage
            containing prediction.
        """
        if not isinstance(message, MotionVectorMessage):
            raise TypeError(f"Message {message} is not of type MotionVectorMessage.")
        # PROCESSING MESSAGE HERE, OBJECT DETECTION...
        detection_msg = DetectionVectorMessage(
            1720246845, "Frame_1", 44, 55, 200, 200, [0.2, 0.8]
        )
        return detection_msg
