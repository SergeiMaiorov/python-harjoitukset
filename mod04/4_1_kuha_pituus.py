# arvioni onko kuha
kuhan_pituus = float(input("Anna kuhan pituus santimetrin(cm): "))

# jos kuha alamitan
if kuhan_pituus < 37:

    # montako senttiä alimmasta sallitusta pyyntimitasta puuttuu
    puuttuu = 37 - kuhan_pituus
    # tulostetaan
    print("Hei Kuha takainsin järveen! Kuha on 37 cm  alamittainen.")
    print(f"alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} santimetrin(cm).")
