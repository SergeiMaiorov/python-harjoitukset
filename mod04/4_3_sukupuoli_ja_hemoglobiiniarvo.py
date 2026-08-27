# kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l)
sukupuoli = input("Anna sinun biologisen sukupuolen: ")
hemoglobiiniarvon = float(input("Anna sinun hemoglobiiniarvon (g/l): "))
# Tulostaa
print("Tuloksesi.")

# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l. ja Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
if sukupuoli == "nainen" or sukupuoli == "Nainen":
    if hemoglobiiniarvon < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvon > 175:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "mies" or sukupuoli == "Mies":
    if hemoglobiiniarvon < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvon > 195:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")

# Jos virhe
else:
    print("Sukupuoli-kentälle syötettiin virheellinen arvo!")
