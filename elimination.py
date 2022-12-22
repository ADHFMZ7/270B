from fractions import *
import random

class Matrix:
  
  def __init__(self, mat):
    self.A = mat 
    self.printmat()

  #print 2d array as matrix
  def printmat(self):
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    print('\n'.join([item for item in row]) 
      for row in self.A]))

  #interchanges 2 rows of a matrix
  def interchange(self, r1, r2):
    A = self.A 
    A[r1], A[r2] = A[r2], A[r1]
    print(f"R{r1}<->R{r2}")

  #adds the elements of row 1 to row 2 
  def matadd(self, r1, s, r2):
    A = self.A
    for i in range(len(A[0])):
      A[r1][i] += s*(A[r2][i])
    print(f"R{r1}+{s}R{r2}")

  #multiplies elements of a row by a scaler
  def s_mul(self, r, s):
    A = self.A 
    for i in range(len(A[0])):
      A[r][i] *= s
    print(f"{s}R{r}") 

  def matmul(self, )


def elimination(matrix):
  pass
