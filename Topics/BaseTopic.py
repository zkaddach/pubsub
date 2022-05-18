from __future__ import annotations
from typing import TYPE_CHECKING, Callable, List

if TYPE_CHECKING:
    from Messages import BaseMessage
    from IpcSharedData import SubscribersPipeConnections
from abc import ABC, abstractmethod
import weakref


class BaseTopic(ABC):
    """
    Base class to create and manage topics.

    Parameters
    ----------
    subs_pipe_conn: SubscribersPipeConnections, default=None
        Object to allow inter-processes communication to subscribed objects
        using pipes.

    multiprocessing: bool, default=True
        Boolean to enable multiprocessing for the created topic.

    Attributes (class)
    ----------
    _instances: [BaseTopic], default=[]
        Stores all instances of topics for current process.

    _local_subscriptions: List[Callable]
        Stores subscribers callback method on new messages.

    Attributes (object)
    ----------
    subs_pipe_conn: SubscribersPipeConnections, default=None
        Object to allow inter-processes communication to subscribed objects
        using pipes.

    multiprocessing: bool, default=True
        Boolean to enable multiprocessing for the created topic.

    Examples
    --------
    >>> from Messages import BaseMessage
    >>> from Subscribers import BaseSubscriber
    >>> from Publishers import BasePublisher
    >>> from Topics import BaseTopic
    >>> from IpcSharedData import SubscribersPipeConnections
    >>>
    >>> # Creating a topic
    >>> subs_pipe_conn = SubscribersPipeConnections()
    >>> topic = BaseTopic(True,subs_pipe_conn)
    >>>
    >>> # Subscribing to the topic
    >>> subscriber = BaseSubscriber()
    >>> subscriber.subscribe(topic)
    >>>
    >>> # Publishing to the topic
    >>> publisher = BasePublisher(topics=[topic])
    >>> publisher.publish(BaseMessage())
    """

    _instances: List[BaseTopic] = []
    _local_subscriptions: List[Callable] = []

    def __init__(
        self,
        multiprocessing: bool = False,
        subs_pipe_conn: SubscribersPipeConnections = None,
    ) -> None:
        self.__class__._instances.append(weakref.proxy(self))
        self.subs_pipe_conn = subs_pipe_conn
        self.is_multiprocessing = multiprocessing

        if (
            self.is_multiprocessing
            and self.subs_pipe_conn
            and self.name() not in self.subs_pipe_conn.keys()
        ):
            self.subs_pipe_conn.register(self.name())

    def _add_subscription(self, subscriber_callback: Callable) -> bool:
        """
        Adds the subscriber callback method, allowing topic to
        send it new message published.
        This method is either a subscriber method (for non-multiprocessing topics)
        or a Pipe.Connection.send method.

        Parameters
        ----------
        subscriber_callback: Callable
            Method allowing topic to send to subscribers new messages.

        Returns
        -------
        bool
            True if callback added successfully, False otherwise.
        """

        try:
            if self.is_multiprocessing and self.subs_pipe_conn:
                self.subs_pipe_conn.add(
                    topic_name=self.name(), subscriber_callback=subscriber_callback
                )
            else:
                self.__class__._local_subscriptions.append(subscriber_callback)
            return True
        except KeyError as err:
            return False

    @classmethod
    def get_instances(cls):
        """Returns all instances of current topic.

        Returns
        -------
        [BaseTopic]
            list of topic instances.
        """
        return cls._instances

    @staticmethod
    @abstractmethod
    def name():
        """Returns the name of the topic.

        Returns
        -------
        str
            Name of the current topic.
        """
        return "BasicTopic"

    def publish(self, message: BaseMessage) -> bool:
        """Publish a message on this topic.
        Sends the message to all subscribers using multiprocessing pipes
        stored in SubscribersPipeConnections object.

        Parameters
        ----------
        message: BaseMessage
            message to be published to this topic.

        Returns
        -------
        bool
            True if message has been transmitted to all subscribers,
            False otherwise.
        """
        try:
            if self._subscriptions:
                for subscriber_callback in self._subscriptions:
                    subscriber_callback(message)
                return True
            else:
                return False
        except KeyError as err:
            print(err)
            # @TODO add message to a local queue
            return False
        except Exception as err:
            print(err)
            # @TODO add message to a local queue
            return False

    def subscribe(self, subscriber_callback: Callable) -> bool:
        """Subscribe objects to this topic.
        Subscription is realised by storing the subscriber pipe connection into
        shared object SubscribersPipeConnections.

        Parameters
        ----------
        subscriber_callback: Callable
            Send method of the pipe connection object of the subscriber.

        Returns
        -------
        bool
            True if subscription is successful, False otherwise.
        """
        return self._add_subscription(subscriber_callback)

    @property
    def _subscriptions(self) -> List[Callable] | None:
        """
        Return the list of all subscribers callback methods.

        Returns
        -------
        List[Callable]
            List of all subscribers callback methods.
        """

        if self.is_multiprocessing and self.subs_pipe_conn:
            if not self.subs_pipe_conn.get(self.name()):
                raise KeyError(f"Topic {self.name()} has no subscriptions.")
            return self.subs_pipe_conn.get(self.name())
        else:
            return self.__class__._local_subscriptions
