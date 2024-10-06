from numpy import *
from sympy import *

'''
Seksjon 4.5
Oppgave 3a
'''

A3 = matrix([[1, -2, 3, -1],
             [2, 3, -1, 3],
             [0, -1, 2, -2],
             [-2, 2, -1, 3]])

A3inv = linalg.inv(A3)

'''
Seksjon  4.5
Oppgave 4a
'''

A4 = matrix([[2, -1, 3],
             [0, -1, 2],
             [-4, 3, 1]])

b4 = matrix([[-1], [2], [3]])

x = linalg.solve(A4, b4)


# eksempler
C = array([[2, -3, 1, 7, 4],
            [0, 1, -3, 2, 5],
            [-4, 2, 1, -1, 3]], dtype=float)

print(C, end="\n\n")

# 2 * R1
C[0, :] = 2*C[0, :]
print(C, end="\n\n")

# R3 + R1
C[2, :] = C[2, :] + C[0, :]
print(C, end="\n\n")

# 1/4 * R1
C[0, :] = (1/4)*C[0, :]
print(C, end="\n\n")

# R3 + 4R2
C[2, :] = C[2, :] + 4*C[1, :]
print(C, end="\n\n")

# R1 + R2
C[0, :] = C[0, :] + C[1, :]
print(C, end="\n\n")

# -1/9 * R3
C[2, :] = C[2, :] * (-1/9)
print(C, end="\n\n")

#R1 + 3*R3
#R2 + 3*R3
C[0, :] = C[0, :] + 3*C[2, :]
C[1, :] = C[1, :] + 3*C[2, :]
print(C, end="\n\n")

A = matrix([[2, -1, 3],
            [0, -1, 2],
            [-4, 3, 1]])

b = matrix([[-1, 2, 3]])

# xA = b      <=>      xAA^{-1} = bA^{-1}       <=>      x = bA^{-1}

Ainv = linalg.inv(A)

x = matmul(b, Ainv)


# oppgave 4 sek 4.6
A4 = Matrix([[1, 2, 5, 2, 7],
            [0, 1, -7, -1, 4],
            [-1, 3, 6, 0, -3],
            [2, -4, 3, 3, 1]])
#           x1  x2  x3 x4 x5

redusert4, pivot = A4.rref()


# oppgave 6 sek 4.6
A6 = Matrix([[1, 0, 2, -1, 0],
            [-2, -3, -7, 3, 2],
            [3, 4, 10, -1, 1],
            [2, 1, 5, 2, 0]])
#           x1  x2  x3 x4 x5

redusert6, pivot = A6.rref()


A8a = Matrix([[2, -4, 1],
            [-1, 2, 3]])

redusert8a, pivot = A8a.rref()

A8b = Matrix([[1, 0, 2, 2],
              [3, 2, 8, 3],
              [-1, 1, 0, 1]])

redusert8b, pivot = A8b.rref()