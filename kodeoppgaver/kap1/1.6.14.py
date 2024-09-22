import numpy as np

'''
    Oppgave 14: 'Bruk MATLAB / Python til å løse oppgavene 1-3, seksjon 1.6
 
    Løsning:  bruker NumPy

'''


# hjelpefunksjon:   printing av matrise
def matprint(matrix):
    formatted_rows = [" ".join([f"{num:3}" for num in row]) for row in matrix]
    formatted = "[[" + formatted_rows[0] + "]"
    for row in formatted_rows[1:]:
        formatted += "\n " + "[" + row + "]"
    formatted += "]"
    return formatted


# hjelpefunksjon:   printing av oppgave
def printoppgave(A, B, AB, BA, oppg):
    print(f'\n========== {oppg} ==========')
    print(f'A:\n{matprint(A)}\n')
    print(f'B:\n{matprint(B)}\n')
    if AB is not None: print(f'AB:\n{matprint(AB)}\n')
    if BA is not None: print(f'BA:\n{matprint(BA)}\n')


# Oppgave 1
def oppg1():
    print("\n\n[ Oppgave 1 ]")

    # deloppgave a)
    A = np.array([[1, -2], [3, 1]])
    B = np.array([[2, -1], [1, 2]])

    # matrise-multiplikasjon
    AB = np.matmul(A, B)
    BA = np.matmul(B, A)

    printoppgave(A, B, AB, BA, "a)")

    # deloppgave b)
    A = np.array([[1, -1, 0], [-2, 0, 1], [-1, 2, 1]])
    B = np.array([[0, 2, 1], [-1, -2, 0], [3, -1, 2]])

    AB = np.matmul(A, B)
    BA = np.matmul(B, A)

    printoppgave(A, B, AB, BA, "b)")


# oppgave 2
def oppg2():
    print("\n[ Oppgave 2 ]")

    A = np.array([[1, -2, 3], [0, -1, 2]])
    B = np.array([[2, 1], [0, -3], [1, 0]])

    AB = np.matmul(A, B)

    printoppgave(A, B, AB, None, "==")


# oppgave 3
def oppg3():
    print("\n[ Oppgave 3 ]")

    A = np.array([1, -2, 3, 0, -1, 2]).reshape(3, 2)
    B = np.array([2, 1, 0, -3, 1, 1]).reshape(2, 3)

    AB = np.matmul(A, B)

    printoppgave(A, B, AB, None, "==")


oppg1()
oppg2()
oppg3()
