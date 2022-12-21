from yapc import expect


def test_assertions_str():
    # tobe
    expect("foobar").to.be("foobar")
    expect("foo")._not.to.be("bar")
    # tohave
    expect("foobar").to.have.string("bar")
    expect("foo")._not.to.have.string("bar")
    # tohave string
    expect("foobar").to.have.str("bar")
    expect("foo")._not.to.have.str("bar")


def test_assertions_str_and():
    expect("foobar").to.be("foobar")._and._not.to.be("bar")
    expect("foo")._not.to.be("bar")
    expect("foo")._not.to.be("bar")
    expect("foobar").to.have.string("bar")
    expect("foo")._not.to.have.string("bar")
    expect("foobar").to.have.str("bar")
    expect("foo")._not.to.have.str("bar")


def test_assertions_str_ok():
    expect("foobar").to.be.ok
    expect("")._not.to.be.ok
