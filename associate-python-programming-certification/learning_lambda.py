def square(num):
  return num * num

square_lambda = lambda num: num * 1

assert square_lambda(2) == square(2)
