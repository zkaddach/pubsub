from .BaseSharedData import BaseSharedData
from typing import Callable, List, Dict


class SubscribersPipeConnections(BaseSharedData):
    """
    Stores subscribers pipe connections send method.
    This class allows topic to send data to subscribers through
    multiprocessing pipe connection.

    Attributes
    ----------
    _senders: Dict[str, List[Callable]]
        Stores a list of pipe connection send methods per topic,
        keys are topic names.
    """

    def __init__(self):
        super(SubscribersPipeConnections, self).__init__()
        self._senders: Dict[str, List[Callable]] = {}

    def add(self, topic_name: str, subscriber_callback: Callable) -> None:
        """
        Adds Pipe.Connection.send method of a subscriber (running on a different process).
        To be used by topics.

        Parameters
        ----------
        topic_name: str
            Name of the topic. Used as key for appending the new subscriber's callback.

        subscriber_callback: Callable
            Pipe.Connection.send method used to send BaseMessage objects to subscriber
            (which is running on a different process).

        Returns
        -------
        None
        """

        self._senders[topic_name].append(subscriber_callback)

    def get(self, topic_name: str) -> List[Callable] | None:
        """
        Get all Pipe.Connection.send methods for all subscribers of the topic with topic_name.

        Parameters
        ----------
        topic_name: str
            Name of the topic for which to retrieve subscribers Pipe.Connection objects.

        Returns
        -------
        List[Callable]
            List of Pipe.Connection.send methods.
        """

        return self._senders.get(topic_name)

    def keys(self) -> List[str]:
        """
        Get all topic names defined for a multiprocessing use case.

        Returns
        -------
        List[str]
            List of all topic names.
        """

        return list(self._senders.keys())

    def register(self, topic_name: str) -> None:
        """
        Register a new topic for multiprocessing usage.
        Creates a new list for this topic name.

        Parameters
        ----------
        topic_name

        Returns
        -------

        """

        if not self._senders.get(topic_name):
            self._senders[topic_name] = []
