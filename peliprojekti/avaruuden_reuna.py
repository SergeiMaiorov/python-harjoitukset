nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

if ikä < 12:
    print("Olet alaikäinen ja ohjelma sammuu!")
else:
    print(f"Tervetuloa, {nimi}!\nVahvistettu ikä {ikä} vuotta!")
    
    tavarat = []

    def pelaa():
        print("Metsäseikkailu alkaa!")
        esine = input("Mitä löysit? ")
        tavarat.append(esine)
        print(f"{esine} lisätty reppuun.")

    def nayta_reppu():
        if len(tavarat) == 0:
            print("Reppu on tyhjä.")
        else:
            print("Repussa on:")
            for esine in tavarat:
                print(esine)

    def nayta_tilanne():
        print(f"Pelaaja: {nimi}")

    komento = ""
    
    while komento != "lopeta":
        print("\n--- Päävalikko ---")
        print("Komennot: pelaa, reppu, tilanne, lopeta")
        komento = input("Anna komento: ")

        if komento == "pelaa":
            pelaa()
        elif komento == "reppu":
            nayta_reppu()
        elif komento == "tilanne":
            nayta_tilanne()
        elif komento == "lopeta":
            print("Näkemiin!")
        else:
            print("Tuntematon komento, yritä uudelleen.")