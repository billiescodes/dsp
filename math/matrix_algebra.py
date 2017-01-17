# Matrix Algebra

#!/usr/bin/Python
# -*- coding: utf-8 -*-

#billiescodes 2017
import numpy as np


A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1],[8],[0],[5]])


## Matrix Dimensions
A.shape #(2,3)
B.shape #(2,2)
C.shape #(3,2)
D.shape #(2,3)
u.shape #(1,4)
v.shape #(1,4)
w.shape #(4,1)


## Vector Operations
a = 6         # Given.

u + v                # array([[ 9,  7, -4,  9]])
u - v                # array([[ 3, -3, -2,  1]])
a * u                # array([[ 36,  12, -18,  30]])
np.inner(u, v)       # array([[51]])
linalg.norm(u)       # 8.6023252670426267

## Matrix operations
#A + C                       # ValueError (not defined)
A - C.T                     # array([[-4, -7, -3],[ 3,  6,  4]])
C.T + (3*D)                 # array([[14,  3,  3],[ 2,  7,  9]])
np.dot(B, A)                # array([[-1, -5, -1],[ 2,  7,  4]])
#np.dot(B, A.T)              # ValueError (not defined)
#np.dot(B, C)                # ValueError (not defined)
np.dot(C, B)                # array([[ 5, -6],[ 9, -8],[ 6, -6]])
np.linalg.matrix_power(B, 4)   # array([[ 1, -4],[ 0,  1]])       
np.dot(A, A.T)              # array([[14, 28],[28, 69]])
np.dot(D.T, D)              # array([[10, -4,  0],[-4,  8,  8],[ 0,  8, 10]])



print np.linalg.matrix_power(B,4)


