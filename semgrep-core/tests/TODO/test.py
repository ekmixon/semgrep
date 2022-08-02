import foobar


def foo():
    # x = { "fld1": "eval" }
    # x.fld2 = "eval"
    return 0


def bar():
    if 1 == 2:
        return 0
    if 1 + 2 == 1 + 2:
        return 1
    if x == x:
        foo()
        bar()
    foo()
    foo()
    foo()
    foo()


def funcs():
    foo(1)
    foo(1, 2)
    foo(1, 2, 3)


def cond():
    bar()
    return False


def stupid_if():
    if foo() > 2:
        foo()
    else:
        foo()

    bar()
