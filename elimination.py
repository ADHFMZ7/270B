import random



#prints 2d array as matrix
def printmat(matrix): 
  for i in matrix:
    print(i)

#interchanges 2 rows of a matrix
def interchange(matrix, r1, r2):
  A = matrix 
  A[r1], A[r2] = A[r2], A[r1]
  print(f"R{r1}<->R{r2}")
  return A

#adds the elements of a row to another
def matadd(matrix, r1, r2):
  A = matrix
  for i in range(len(A[0])):
    A[r1][i] += A[r2][i]

  print(f"R{r1}+R{r2}")
  return A
    
def elimination(matrix):
  pass

a = [[random.randint(0, 9) for j in range(10)]for i in range(5)]
printmat(a)
printmat(interchange(a, 1, 2))
printmat(matadd(a, 1, 2))
