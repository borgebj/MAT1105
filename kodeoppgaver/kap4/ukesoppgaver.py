from numpy import *

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

