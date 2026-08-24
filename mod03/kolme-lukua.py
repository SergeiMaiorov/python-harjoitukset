## Pyydä kolme kokonaislukua
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))


##lasken lukujen summan

summan = luku1 + luku2 + luku3


##lasken lukujen tulon
tulo = luku1 * luku2 * luku3

##lasken lukujen keskiarvon
keskiarvo = summan / 3


##tulostaa lukujen summan, tulon ja keskiarvon
print(f"Lukujen summa on: {summan}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo}")
