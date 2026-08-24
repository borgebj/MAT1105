from sympy import Matrix


counter = 0


with open("input.txt") as f:
    data = [line for line in f.read().splitlines() if line.strip()]

for i in range(0, len(data), 3):
    chunk = data[i:i+3]

    # ============== parsing ==============
    _, _, xa, ya = chunk[0].split()
    _, _, xb, yb = chunk[1].split()
    _, resx, resy = chunk[2].split()

    xa = xa.split('+')[1].replace(",", "")
    ya = ya.split('+')[1].replace(",", "")

    xb = xb.split("+")[1].replace(",", "")
    yb = yb.split("+")[1].replace(",", "")

    resx = int(resx.split("=")[1].replace(",", "")) + 10000000000000
    resy = int(resy.split("=")[1].replace(",", "")) + 10000000000000

    # make vectors
    col1 = Matrix([xa, ya])
    col2 = Matrix([xb, yb])
    col3 = Matrix([resx, resy])

    # combine vectors to matrix
    A = Matrix.hstack(col1, col2, col3)

    # compute RREF
    rref, pivot = A.rref()

    # retrieve last column
    result = rref[:, -1]

    if result[0].is_integer and result[1].is_integer:
        counter += result[0] * 3
        counter += result[1]


print(counter)
