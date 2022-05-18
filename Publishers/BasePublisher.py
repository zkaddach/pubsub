from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from Topics import BaseTopic
    from Messages import BaseMessage
from abc import ABC, abstractmethod


class BasePublisher(ABC):
    """
    Base abstract class for publishers.

    Parameters
    ----------
    topics: List[BaseTopic]
        List of topics to publish to.

    Attributes (class)
    ----------
    _pub_topics:  List[BaseTopic]
        List of topics to publish to.
    """

    _pub_topics: List[BaseTopic] = []

    def __init__(self, topics: List[BaseTopic] = None):
        if topics is None:
            topics = []
        self.__class__._pub_topics.extend(topics)

    def add(self, topic: BaseTopic) -> None:
        """
        Adds topic to the list of topics to publish to.

        Parameters
        ----------
        topic: BaseTopic
            Topic to add in list of topics to publish to.

        Returns
        -------

        """

        self.__class__._pub_topics.append(topic)

    def publish(self, message: BaseMessage) -> None:
        """
        Publish message to all topics added in the list of topics
        to publish to.

        Parameters
        ----------
        message: BaseMessage
            Message to publish.

        Returns
        -------

        """
        for topic in self.__class__._pub_topics:
            topic.publish(message)

    @staticmethod
    @abstractmethod
    def name():
        """Returns the name of the Publisher.

        Returns
        -------
        str
            Name of the current publisher type.
        """

        return "BasePublisher"
