# (LUX, A, B, C)
hyttiluokka = input("Anna hyttiluokka(LUX/lux, A/a, B/b, C/c): ")

# Valintarakenne (if), kun monta vaihtoehtoa
if hyttiluokka == "LUX" or hyttiluokka == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A" or hyttiluokka == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B" or hyttiluokka == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C" or hyttiluokka == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")

    # Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa
else:
    print("Virheellinen hyttiluokka.")
