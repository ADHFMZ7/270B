def factorial(n):
  if n in [0, 1]:
    return 1
  return factorial(n-1) * n

def sin(x):
  result = 0
  for n in range(100):
    result += pow(-1, n)  * (pow(x, 2*n+1)/factorial(2*n+1))
  return result

def cos(x, accuracy = 100):
  return sum([pow(-1, n) * (pow(x, 2*n)/factorial(2*n)) for n in range(accuracy)])
