from yapc import expect


def test_assertions_str_contains_str():
    expect("foobar").to.have.string("bar")
