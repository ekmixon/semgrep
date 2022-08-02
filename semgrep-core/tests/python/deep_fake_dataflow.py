def foo():
  bar()
  #ERROR: match
  x = requests.get("foo")
  bar()
  render(o.format(x))

