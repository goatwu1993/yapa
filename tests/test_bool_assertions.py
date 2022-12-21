from yapc import expect


def test_bool_ok():
    expect(True).to.be.ok
    expect(False).to.be._not.ok
    expect(True).to.be.true
    expect(False).to.be.false
    expect(True)._not.to.be.false
    expect(False)._not.to.be.true
