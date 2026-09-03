teksti = input("Anna luku: ")

if teksti != "":
    pienin = float(teksti)
    suurin = float(teksti)

    teksti = input("Anna luku: ")
    while teksti != "":
        luku = float(teksti)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku
        teksti = input("Anna luku: ")

    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
