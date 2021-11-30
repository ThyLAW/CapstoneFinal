import curl


def test_xss():
    assert curl.xss() == 0
