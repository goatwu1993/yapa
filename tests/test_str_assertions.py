from yapa import expect


def test_assertions_str_positive():
    # tobe
    expect("foobar").to_be("foobar")
    expect("foobar").to_contain("bar")
    expect("foobar").to_be_truthy()
    expect("foobar").to_be_identical_to("foobar")
    expect("foobar").to_be_lowered()
