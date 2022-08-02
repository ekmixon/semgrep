
#ERROR:
if A:
  if B:
    foo()

  if C and B:
    foo()

  if C and D and B:
    foo()

  foo()
