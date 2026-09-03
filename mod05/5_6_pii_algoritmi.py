import random

N = int(input("Anna arvottavien pisteiden määrä: "))
toistot = 0
n = 0

while toistot < N:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    if x**2 + y**2 < 1:
        n = n + 1

    toistot = toistot + 1

pii = 4 * n / N
print(f"Piin likiarvo: {pii}")