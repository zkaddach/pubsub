from Messages import DetectionVectorMessage


def test_init():
    msg = DetectionVectorMessage(
        1720246845, "Frame_1", 44, 55, 200, 200, [0.2, 0.8]
    )
    assert isinstance(msg.timestamp, int)


def test_name():
    msg = DetectionVectorMessage(
        1720246845, "Frame_1", 44, 55, 200, 200, [0.2, 0.8]
    )
    assert msg.name() == "DetectionVectorMessage"


def test_prediction_vector():
    msg = DetectionVectorMessage(
        1720246845, "Frame_1", 44, 55, 200, 200, [0.2, 0.8]
    )
    assert sum(msg.class_prediction) == 1
