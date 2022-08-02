def wrapper():
    return source1()

a = wrapper()
b = a
b = sanitize1()
#ERROR:
sink1(b)
