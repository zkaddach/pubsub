from Messages import MotionVectorMessage


def test_init():
    msg = MotionVectorMessage(
        1720246845, "Frame_1", 44, 55, 200, 200, [[2, 4], [3, 6]]
    )
    assert isinstance(msg.timestamp, int)


def test_name():
    msg = MotionVectorMessage(
        1720246845, "Frame_1", 44, 55, 200, 200, [[2, 4], [3, 6]]
    )
    assert msg.name() == "MotionVectorMessage"
