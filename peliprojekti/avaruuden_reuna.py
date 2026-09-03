# kysyy pelaajan nimi ja ikä

nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

if ikä < 12:
    print("Olet alaikäinen ja ohjelma sammuu!")
else:
    print(f"Tervetuloa, {nimi}!\nVahvistettu ikä {ikä} vuotta!")
    komento = ""

    while komento != "lopeta":
        print("\n--- Päävalikko ---")
        print("Komennot: pelaa, reppu, lopeta")
        komento = input("Anna komento: ")

        if komento == "pelaa":
            print("Metsäseikkailu alkaa!")
        elif komento == "reppu":
            print("Repussa on miekka ja 5 omenaa.")
        elif komento == "lopeta":
            print("Näkemiin!")
        else:
            print("Tuntematon komento, yritä uudelleen.")


# Tulosta konsoliin
# print(f"Tervetuloa, {nimi}!\n Vahvistettu ikä {ikä} vuotta!")
