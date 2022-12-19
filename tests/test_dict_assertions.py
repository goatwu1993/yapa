from yapc import expect


def test_assertions_str_contains_str():
    expect({"a": 1, "b": 2}).to.have.all.keys("a", "b")
    expect({"a": 1, "b": 2}).to.have.keys("a", "b")
