def test_title():
    assert "SATC" in open("index.html").read()


def test_student():
    assert "CT.2023.S0G8C5" in open("index.html").read()
