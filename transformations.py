

# transforms vector by multiplying by a transformation matrix 
def matmul(mat1, mat2):
  if len(mat1[0]) != len(mat2):
    raise Exception("matrices can not be multiplied")
  
  
A = [[1, 2, 3], #3x3 matrix
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 3], #2 x 3 matrix
     [6, 5, 4]]

print(matmul(B, A))

