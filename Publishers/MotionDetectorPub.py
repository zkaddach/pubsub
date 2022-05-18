from Publishers.BasePublisher import BasePublisher


class MotionDetectorPub(BasePublisher):
    """
    Publisher for Motion detection vectors.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def name():
        """Returns the name of the Publisher.

        Returns
        -------
        str
            Name of the current publisher type.
        """

        return "MotionDetectorPub"
