
#tietojen yhdistäminen ja tuominen "luokat.py" tiedostosta 
from luokat import Esine, Huone,Pelaaja

"""
Tarina: Olet avaruuslentäjä. 
Aluksesi on rikki. 
Tavoite: Etsi moottori ja korjaa alus.
"""

print(" <<<<--Avaruuden reuna-->>>>\n ")
print("Tarina: Olet avaruuslentäjä. Aluksesi on rikki.\n")
print("Tavoite: Etsi moottori ja korjaa alus.\n")


nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

# iän vahvistuslohko
if ikä < 12:
    print("Olet alaikäinen ja ohjelma sammuu!")
else:
    print(f"Tervetuloa, {nimi}!\nVahvistettu ikä {ikä} vuotta!\n")
    
# Kartta
    huone1 = Huone("Ohjaamo", "Täällä ohjataan alusta")
    huone2 = Huone("Käytävä", "Pitkä ja kylmä käytävä")
    huone3 = Huone("Varasto", "Pimeä huone")

    huone1.add_exit("Eteen", huone2)
    huone2.add_exit("Taakse", huone1)
    huone2.add_exit("Oikea", huone3)
    huone3.add_exit("Vasemmalle", huone2)

    moottori = Esine("Moottori", 15.5)
    huone3.esine = moottori

    pelaaja = Pelaaja(nimi, huone1)    
    
    
# tavarat

        
    def pelaa():
        suunta = input("Anna suunta (eteen/taakse/oikea/vasemmalle): ").strip().upper()
        pelaaja.liiku(suunta)
        
    def keraa():
        pelaaja.keraa_esine()

    def nayta_reppu():
        #if len(tavarat) == 0:
        if len(pelaaja.reppu) == 0:
            print("Reppu on tyhjä")
        else:
            print("Repussa on:")
            #   print(esine)
            for esine in pelaaja.reppu:
                print(f" {esine.nimi}")

    def nayta_tilanne():
        #print(f"Pelaaja: {nimi}")
        print(f"Pelaaja: {pelaaja.nimi}")
        print(f"Sijainti: {pelaaja.sijainti.nimi} - {pelaaja.sijainti.kuvaus}")
    
    
#Päävalikko
    komento = ""

    while komento != "lopeta":
        print("\n--- Päävalikko ---")
        print("Komennot: liiku, keraa, reppu, tilanne, lopeta")
        komento = input("Anna komento: ").strip().lower()

        if komento == "liiku":
            pelaa()
        elif komento == "keraa":
            keraa()
        elif komento == "reppu":
            nayta_reppu()
        elif komento == "tilanne":
            nayta_tilanne()
        elif komento == "lopeta":
            print("Näkemiin!")
        else:
            print("Tuntematon komento, yritä uudelleen.")