from multiprocessing.managers import SyncManager
from IpcSharedData.SubscribersPipeConnections import SubscribersPipeConnections
from typing import Any


class PubSubManager(SyncManager):
    """
    Multiprocessing manager.
    Register data types (classes) which we would like to share across
    our processes.

    Attributes
    ----------
    SubscribersPipeConnections: SubscribersPipeConnections
        Class for sharing subscribers pipe connection end.
    """

    def __init__(self):
        super().__init__()
        self.SubscribersPipeConnections: Any


PubSubManager.register(
    "SubscribersPipeConnections",
    SubscribersPipeConnections,
)
