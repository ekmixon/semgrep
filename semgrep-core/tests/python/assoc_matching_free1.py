
#OK:
if A or B:
  foo()

# OK
if A or C:
  foo()

#ERROR:
if A or B:
  foo()

#ERROR:
if A or B:
  foo()

#OK:
if A or B or C:
  foo()

#OK:
if B or C:
  foo()
