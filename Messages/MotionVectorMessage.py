from .BaseMessage import BaseMessage
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class MotionVectorMessage(BaseMessage):
    """
    Motion vector messages.

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
    velocity: [[]]
        speed and direction of the detected motion.

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
    velocity: [[]]
        speed and direction of the detected motion.

    Examples
    --------
    >>> from Messages import MotionVectorMessage
    >>> msg = MotionVectorMessage(
    >>>     1720246845, 'Frame_1', 44, 55, 200, 200, [[2, 4], [3, 6]]
    >>> )
    >>> print(msg)
    """

    timestamp: int
    frame_id: str
    bb_x: int
    bb_y: int
    bb_w: int
    bb_h: int
    velocity: List[List[float]]
    image_resolution: Tuple[int, int] = (600, 480)

    def _validate(self):
        """Checks that data is valid.

        Returns
        -------
        bool
            True if data is valid, False otherwise.
        """

        # Check bounding box position
        if not 0 <= self.bb_x <= self.image_resolution[0]:
            return False
        if not 0 <= self.bb_y <= self.image_resolution[1]:
            return False
        return True

    def name(self):
        """Returns the name of the message.

        Returns
        -------
        str
            Name of the current message type.
        """

        return "MotionVectorMessage"
