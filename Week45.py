from functools import reduce
c = [10, 24, 34, 42, 19]
s = reduce(lambda a, b : a + b, c)
l = reduce(lambda a, b : a * b, c)
print(s, l)
