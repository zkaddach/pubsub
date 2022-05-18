from abc import ABC, abstractmethod
from Messages import BaseMessage
from typing import Any


class BaseProcessor(ABC):
    """
    Base processor abstract class to process messages.
    """

    def __init__(self):
        pass

    @abstractmethod
    def process(self, message: BaseMessage) -> Any:
        """Method which process the message.

        Parameters
        ----------
        message: BaseMessage
            Message to process.

        Returns
        -------
        Any
            Depends on the process to apply, can return anything.
        """
        pass
