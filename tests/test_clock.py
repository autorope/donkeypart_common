from donkeypart_common import Timestamp


def test_timestamp():
    ts = Timestamp()
    time = ts.run()
    assert time is not None