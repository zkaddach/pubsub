from abc import ABC, abstractmethod


class BaseMessage(ABC):
    """
    Base abstract class for topic messages.
    """

    def __init__(self):
        pass

    @abstractmethod
    def _validate(self):
        """Checks that data is valid.

        Returns
        -------
        bool
            True if data is valid, False otherwise.
        """

        pass

    @abstractmethod
    def name(self):
        """Returns the name of the message.

        Returns
        -------
        str
            Name of the current message type.
        """

        return "BaseMessage"
