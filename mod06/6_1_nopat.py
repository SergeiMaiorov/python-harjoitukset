import random

teksti = input("Kuinka monta noppaa? ")
maara = int(teksti)

summa = 0

for i in range(maara):
    silmaluku = random.randint(1, 6)
    summa = summa + silmaluku

print(summa)