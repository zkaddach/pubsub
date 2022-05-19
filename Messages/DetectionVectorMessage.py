from .BaseMessage import BaseMessage
from dataclasses import dataclass
from typing import List


@dataclass
class DetectionVectorMessage(BaseMessage):
    """
    Detection vector messages.

    Parameters
    ----------
    timestamp: int
        Timestamp of the frame.
    frame_id: str
        ID of the frame.
    bb_x: int
        x position of the bounding box.
    bb_y: int
        y position of the bounding box.
    bb_w: int
        width of the bounding box.
    bb_h: int
        height of the bounding box.
    class_prediction: []
        object detection prediction vector.

    Attributes
    ----------
    timestamp: int
        Timestamp of the frame.
    frame_id: str
        ID of the frame.
    bb_x: int
        x position of the bounding box.
    bb_y: int
        y position of the bounding box.
    bb_w: int
        width of the bounding box.
    bb_h: int
        height of the bounding box.
    class_prediction: []
        object detection prediction vector.

    Examples
    --------
    >>> from Messages import DetectionVectorMessage
    >>> msg = DetectionVectorMessage(
    >>>     1720246845, 'Frame_1', 44, 55, 200, 200, [0.2, 0.8]
    >>> )
    >>> print(msg)
    """

    timestamp: int
    frame_id: str
    bb_x: int
    bb_y: int
    bb_w: int
    bb_h: int
    class_prediction: List[float]

    def _validate(self):
        """Checks that data is valid.

        Returns
        -------
        bool
            True if data is valid, False otherwise.
        """

        # check class_prediction vector
        if not sum(self.class_prediction) == 1:
            return False
        return True

    def name(self):
        """Returns the name of the message.

        Returns
        -------
        str
            Name of the current message type.
        """
        return "DetectionVectorMessage"
