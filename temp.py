import sys
import numpy as np
import scipy as sp



from numpy import linalg as LA
from numpy import random
from numpy import matrixlib as ML



print(sys.version)



print('hello world')
print(2**32)

print(sys.platform)  # should be win32 (Why not win64?)
print(2**8)
x = 'Spam!'
print(x*8)

y = 5
print('y = ' + str(y))

chubmub = sys.platform

curVersion = sys.version

print('Version = ', curVersion)

# A comment will look like this.

print('Arguments: ', len(sys.argv))
print('List: ', str(sys.argv))

name = input("Enter a name: ")

print(name)

# myVar = int(input("Enter a number: "))
#
# if myVar==4.0:
#     print("Right you are")
# else:
#     print("Try again")


# for i in range(0,10):
#     for j in range(10,-2,-2):
#         print(i,',',j)


a = np.arange(16).reshape(4, 4)
print(a)

randMat = random.random(16).reshape(4,4)
print('randMat = ', randMat)



rInv = LA.inv(randMat)
print('rInv = ', rInv)

rProd = np.matrix.round(np.matmul(randMat,rInv),2)

print('rProd = ',rProd)

print(type(rProd))

# Adding a comment.
x = np.zeros((2,2), dtype=[('a', np.int32), ('b', np.float64, (3,3))])
print(x['b'])

