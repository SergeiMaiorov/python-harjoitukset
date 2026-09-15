import random,math

pisteiden_määrä = 1000000

laskuri = 0

Ympäripyörän_sisällä = 0

while laskuri < pisteiden_määrä:
    laskuri = laskuri + 1

    x=random.uniform(-1000, 1000) /1000
    y=random.uniform(-1000, 1000) /1000

    if math.sqrt(x**2 + y**2) < 1:
        Ympäripyörän_sisällä = Ympäripyörän_sisällä + 1

print(f"Ympäripyörän sisällä: {Ympäripyörän_sisällä}")