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