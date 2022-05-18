from .BaseTopic import BaseTopic
from .MotionVectorTopic import MotionVectorTopic
from .DetectionVectorTopic import DetectionVectorTopic

TOPIC_BUILDER = {
    "MotionVectorTopic": MotionVectorTopic,
    "DetectionVectorTopic": DetectionVectorTopic,
}

__all__ = [
    "BaseTopic",
    "MotionVectorTopic",
    "DetectionVectorTopic",
    "TOPIC_BUILDER",
]
