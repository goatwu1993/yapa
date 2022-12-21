from yapc import expect


def test_bool_ok():
    expect(True).to.be.ok
    expect(False).to.be._not.ok
    expect(True).to.be.true
    expect(False).to.be.false
    expect(True)._not.to.be.false
    expect(False)._not.to.be.true
    expect(True).to.be.a(bool)
    expect(False).to.be.a(bool)
    expect(True)._not.to.be.a(str)
    expect(False)._not.to.be.a(str)
    expect(True).to.equal(True)
    expect(False).to.equal(False)
    expect(True)._not.to.equal(False)
    expect(False)._not.to.equal(True)
