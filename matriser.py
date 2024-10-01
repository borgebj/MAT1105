
import sympy as sp

A = sp.Matrix([[1, 2],
              [3, 4]])

B = sp.Matrix([[4, 3],
              [2, 1]])

C = sp.Matrix([[2, -1, 4, 5, 6],
               [6, -1, 3, 2, 1],
               [-2, 3, 1, 0, 5]])

AB = A * B

# Redusert Trappeform

reduced_matrix, pivot_columns = C.rref()

# printer fint

sp.pprint(reduced_matrix)

sp.pprint(pivot_columns)

