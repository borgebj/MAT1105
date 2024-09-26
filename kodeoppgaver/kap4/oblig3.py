
import sympy as sp

# [ Seksjon 4.3 - Oppgave 6 ]
A = sp.Matrix([[2, -1, 1, 3, -4],
               [-1, 2, 4, 3, 2],
               [-2, 1, 3, -4, -1]])

redusert, pivot = A.rref()

var = ["x", "y", "z"]

løsninger = {}
for i in range(redusert.rows):
    # Sjekk om det er en pivotelement i denne raden
    if i in pivot:
        # Finn løsningen for den variable som er representert av pivotelementet
        løsninger[f'{var[i]}'] = redusert[i, -1] - sum(redusert[i, j] * løsninger.get(f'Variable_{j}', 0) for j in range(redusert.cols - 1))

# Skriv ut løsningene
for var, value in løsninger.items():
    print(f"{var}: {value}")