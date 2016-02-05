def fib(n,x):
  p = [0, 1]
  while len(p) < n:
    p.append(p[-1] + p[-2])
  return p[x]

 print fib(10,9)