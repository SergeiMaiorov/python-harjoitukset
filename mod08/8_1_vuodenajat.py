vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kk = int(input("Anna kuukauden numero (1-12): "))

if kk == 12 or kk == 1 or kk == 2:
    vuodenaika = vuodenajat[0]  # talvi
elif kk == 3 or kk == 4 or kk == 5:
    vuodenaika = vuodenajat[1]  # kevät
elif kk == 6 or kk == 7 or kk == 8:
    vuodenaika = vuodenajat[2]  # kesä
elif kk == 9 or kk == 10 or kk == 11:
    vuodenaika = vuodenajat[3]  # syksy
else:
    vuodenaika = "Virhe kuukausi"

print(f"Vuodenaika on: {vuodenaika}")
