from yapc import expect


def test_assertions_str_contains_str():
    expect("foobar").to.have.string("bar")
    expect("foo")._not.to.have.string("bar")
    expect("foobar").to.have.str("bar")
    expect("foo")._not.to.have.str("bar")
