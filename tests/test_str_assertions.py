from yapa import expect


def test_assertions_str_positive():
    # tobe
    s = "foobar"
    expect(s).to_be(s)
    expect(s).to_contain("bar")
    expect(s).to_be_truthy()
    expect(s).to_be_identical_to(s)
    expect(s).to_be_lower_case()
    expect(s.upper()).to_be_upper_case()
    expect(s).to_be_identical_to(s)
