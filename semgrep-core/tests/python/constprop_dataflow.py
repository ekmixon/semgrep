def foo1():
    # ERROR:
    x = "x"
    # ERROR:
    y = "y"
    # ERROR:
    t = x + y

def foo2(c):
    a = "a" if c else "b"
    # ERROR:
    v = a


def foo3(c):
    # ERROR:
    x = "hi"
    while c:
        # TODO:
        # OK:
        x = f"{x} hi"
    # ERROR:
    y = x
