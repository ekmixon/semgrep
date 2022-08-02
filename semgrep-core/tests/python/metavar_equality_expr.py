def test_equal():
    a = 1
    b = 2
    # ERROR: match
    return 1 if a + b == a + b else 0
