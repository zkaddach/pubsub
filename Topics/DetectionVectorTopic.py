from .BaseTopic import BaseTopic
from IpcSharedData.SubscribersPipeConnections import SubscribersPipeConnections


class DetectionVectorTopic(BaseTopic):
    """
    Detection vector topic.
    """

    def __init__(
        self,
        multiprocessing: bool = False,
        subs_pipe_conn: SubscribersPipeConnections = None,
    ) -> None:
        super().__init__(multiprocessing, subs_pipe_conn)

    @staticmethod
    def name():
        """Returns the name of the topic.

        Returns
        -------
        str
            Name of the current topic.
        """

        return "DetectionVectorTopic"
