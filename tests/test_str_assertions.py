from yapa import expect


def test_assertions_str_positive():
    # tobe
    expect("foobar").to_be("foobar")
