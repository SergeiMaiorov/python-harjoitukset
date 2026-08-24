## Pyydä kolme kokonaislukua
leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))


##lasken kaikki yhteensä luodit
yhteensä_luodit = (leiviskät * 20 * 32) + (naulat * 32) + luodit

##lasken yhteensä grammaa
## koska yksi luoti on 13,3 grammaa
yhteensä_grammaa = yhteensä_luodit * 13.3


##lasken yhtenespalauttava jakolasku kilogrammaa
##yhtenespalauttava_jakolasku_kilogrammaa
kilogrammat = int(yhteensä_grammaa) // 1000

## lasken jakojäännösoperaatio grammat
##jakojäännösoperaatio_grammat
grammat = yhteensä_grammaa % 1000

##tulostaa täysiksi kilogrammoiksi ja grammoiksi käyttäjälle.
print("Massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat:3.2f} grammaa.")
