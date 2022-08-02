FOOBAR = 42
bar = 'barbar'
#ERROR: match
foo = f"{bar}baz" + f"{FOOBAR}FOO"
#ERROR: match
foo2 = f"{bar}baz" + f"{FOOBAR}FOO" + bar

print(42)
