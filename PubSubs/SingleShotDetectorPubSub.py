from Publishers.BasePublisher import BasePublisher
from Subscribers.BaseSubscriber import BaseSubscriber


class SingleShotDetectorPubSub(BasePublisher, BaseSubscriber):
    """
    Single shot detector publisher and subscriber.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def name():
        """Returns the name of the subscriber.

        Returns
        -------
        str
            Name of the current subscriber/publisher type.
        """
        return "SingleShotDetectorPubSub"
