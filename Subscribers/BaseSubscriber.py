"""
Abstract parent class of Subscribers.
"""

from typing import List, Dict, Any
from abc import ABC, abstractmethod
from multiprocessing import Pipe
from multiprocessing.connection import Connection
from Topics.BaseTopic import BaseTopic
from Messages import BaseMessage


class BaseSubscriber(ABC):
    """
    Base subscriber class.

    Parameters
    ----------

    Attributes (class)
    ----------
    _sub_topics: Dict[str, Dict[str, Any]]
        Subscribed topics.

    _local_message_queue: List[BaseMessage]
        Local queue of message, only used for in-process topics.
    """

    _sub_topics: Dict[str, Dict[str, Any]] = {}
    _local_message_queue: List[BaseMessage] = []

    def __init__(self):
        pass

    def get(self, topic_name: str) -> BaseMessage | None:
        """
        Get next message published in subscribed topics.
        Messages are retrieved in FIFO mode. Messages are received from
        pipe connection or stored in local queue.

        Parameters
        ----------
        topic_name: str
            Topic name from which to get next message.

        Returns
        -------

        """

        if self.__class__._sub_topics[topic_name]["topic"].is_multiprocessing:
            return self.__class__._sub_topics[topic_name]["recv"].recv()
        else:
            try:
                return self.__class__._local_message_queue.pop()
            except IndexError:
                return None

    @staticmethod
    @abstractmethod
    def name():
        """Returns the name of the subscriber.

        Returns
        -------
        str
            Name of the current subscriber type.
        """

        return "BaseSubscriber"

    def push(self, message: BaseMessage):
        """
        Adds new message published on a non-multiprocessing topic,
        to the local queue of messages.

        Parameters
        ----------
        message: BaseMessage
            Message to add to the local queue.

        Returns
        -------

        """

        self.__class__._local_message_queue.insert(0, message)

    def subscribe(self, topic: BaseTopic) -> None:
        """
        Subscribe to a topic.
        A subscriber can subscribe to many topics.

        Parameters
        ----------
        topic: BaseTopic
            Topic to subscribe to.

        Returns
        -------
        bool
            True if subscription was successfull, False otherwise.

        Examples
        --------
        >>> from Topics import MotionVectorTopic
        >>> simple_topic = MotionVectorTopic(multiprocessing=False)
        >>> sub = BaseSubscriber()
        >>> sub.subscribe(simple_topic)
        """

        topic_params: Dict[str, BaseTopic | Connection] = {"topic": topic}
        if topic.is_multiprocessing:
            sub_end, topic_end = Pipe(duplex=False)
            topic.subscribe(topic_end.send)
            topic_params["recv"] = sub_end
        else:
            topic.subscribe(self.push)
        self.__class__._sub_topics[topic.name()] = topic_params

    def subscriptions(self) -> List[str]:
        """
        Retrieve list of topics this subscriber is subscribed to.

        Returns
        -------
        List[str]
            List of topic names this subscriber is subscribed to.
        """

        return list(self.__class__._sub_topics.keys())
