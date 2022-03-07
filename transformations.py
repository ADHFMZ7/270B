# transforms vectors using matrix multiplication

def matmul(mat1, mat2):
  if len(mat1[0]) != len(mat2):
    raise Exception("matrices can not be multiplied")
  

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 3],
     [6, 5, 4]]

