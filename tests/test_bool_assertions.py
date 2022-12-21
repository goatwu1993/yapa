from yapc import expect


def test_bool_ok():
    expect(True).to.be.ok
    expect(False).to.be._not.ok
