from Subscribers.BaseSubscriber import BaseSubscriber


class LoggerSub(BaseSubscriber):
    """
    Logger subscriber class.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def name():
        """Returns the name of the subscriber.

        Returns
        -------
        str
            Name of the current subscriber type.
        """

        return "LoggerSub"
