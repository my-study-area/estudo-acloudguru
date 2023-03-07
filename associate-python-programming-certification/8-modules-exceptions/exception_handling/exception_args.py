from email import message


class ExampleError(Exception):
  pass

def bad_function():
  raise ExampleError("this is a message", 1, 2, 4, 5, 6)

try:
  bad_function()
except ExampleError as err:
  message, x, y, *other = err.args
  print(message)
  print(x + y)
  print(other)
