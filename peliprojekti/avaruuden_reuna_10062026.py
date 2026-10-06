import json
#import os

#tietojen yhdistäminen ja tuominen "luokat.py" tiedostosta 
from luokat import Esine, Huone, Pelaaja

"""
Tarina: Olet avaruuslentäjä. 
Aluksesi on rikki. 
Tavoite: Etsi moottori ja korjaa alus.
"""

#Tein intro.txt ja ohjeet.txt tiedostot
#Minä olen tallennyt pelin tilanne erilliseen tekstitiedostoon, jotta pelaaja voi jatkaa peliä myöhemmin siitä mihin jäi.
# Tein  "Error Handling" esimerkin mukaan https://metropolia-sw.github.io/sw1-python/en/13_file_handling.html
print(" <<<<--Avaruuden reuna-->>>>\n ")
#    pass
try:
    with open("intro.txt", "r") as file:
        intro_teksti = file.read()
        print(intro_teksti)
    with open("instructions.txt", "r") as file:
        ohje_teksti = file.read()
        print(ohje_teksti)
except FileNotFoundError:
# Jos tiedostoa ei löydy, tulostaa varateksti
    print("Tarina: Olet avaruuslentäjä. Aluksesi on rikki.\n")
    print("Tavoite: Etsi moottori ja korjaa alus.\n")




nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

# iän vahvistuslohko
if ikä < 12:
    print("Olet alaikäinen ja ohjelma sammuu!")
else:
    print(f"Tervetuloa, {nimi}!\nVahvistettu ikä {ikä} vuotta!\n")
    
    
##Kartan rakentaminen (add_exit) ja huoneiden yhdistäminen perustuvat Github-käyttäjä AvaHeinonen koodiin osoitteessa https://github.com/AvaHeinonen/RoomGame/blob/main/room_game.py
    
# Kartta
    huone1 = Huone("Ohjaamo", "Täällä ohjataan alusta")
    huone2 = Huone("Käytävä", "Pitkä ja kylmä käytävä")
    huone3 = Huone("Varasto", "Pimeä huone")

    huone1.add_exit("Eteen", huone2)
    huone2.add_exit("Takaisin", huone1)
    huone2.add_exit("Oikea", huone3)
    huone3.add_exit("Vasen", huone2)

    moottori = Esine("Moottori", 15.5)
    huone3.esine = moottori

    pelaaja = Pelaaja(nimi, huone1)    
    
    
# tavarat
    
    """ tavarat = []

    def pelaa():
        print("Metsäseikkailu alkaa!")
        esine = input("Mitä löysit? ")
        tavarat.append(esine)
        print(f"{esine} lisätty reppuun.") """
        
    def pelaa():
        suunta = input("Anna suunta (eteen/takaisin/oikea/vasen): ").strip().upper()
        pelaaja.liiku(suunta)
        
    def keraa():
        pelaaja.keraa_esine()

    def nayta_reppu():
        #if len(tavarat) == 0:
        if len(pelaaja.reppu) == 0:
            print("Reppu on tyhjä")
        else:
            print("Repussa on:")
            #for esine in tavarat:
            #   print(esine)
            for esine in pelaaja.reppu:
                print(f" {esine.nimi}")

    def nayta_tilanne():
        #print(f"Pelaaja: {nimi}")
        print(f"Pelaaja: {pelaaja.nimi}")
        print(f"Sijainti: {pelaaja.sijainti.nimi} - {pelaaja.sijainti.kuvaus}")
    
    
    
# Tein json.dump/json.load "Tiedon serialisointi" kappalle esimerkin mukaan https://metropolia-sw.github.io/sw1-python/en/13_file_handling.html
    def tallenna_peli():  
        tallennus_data = {
        "pelaaja": pelaaja.nimi,
        "huone": pelaaja.sijainti.nimi,
        "taso": 5,
        }
        with open("save.json", "w") as tiedosto:
            json.dump(tallennus_data, tiedosto)
        print(f"Peli tallenettu!")
    
    def lataa_peli():
        try:
            with open("save.json", "r") as tiedosto:
                data_luettu = json.load(tiedosto)
            print("Peli on ladattu : \n")
            print(f"Pelaaja: {data_luettu['pelaaja']}, huone: {data_luettu['huone']}, taso: {data_luettu['taso']}")
        except FileNotFoundError:
            print("Tallenta peliä ei löytynyt. Tiedostoa ei ole löydy.")    
    
"""# Tein "Tiedoston poistaminen" esimerkin mukaan https://metropolia-sw.github.io/sw1-python/en/13_file_handling.html
if os.path.exists("save.txt"):
    os.remove("save.txt")
else:
    print("Tiedostoa ei löydy.") """
    
    
#Päävalikko
    komento = ""

    while komento != "lopeta":
        print() 
        print("-"*50)
        print("\n--- Päävalikko ---")
        print("Komennot: liiku, keraa, reppu, tilanne, tallenna, lataa, lopeta")
        komento = input("Anna komento: ").strip().lower()

        if komento == "liiku":
            pelaa()
        elif komento == "keraa":
            keraa()
        elif komento == "reppu":
            nayta_reppu()
        elif komento == "tilanne":
            nayta_tilanne()
        elif komento == "tallenna":
            tallenna_peli()
        elif komento == "lataa":
            lataa_peli()
        elif komento == "lopeta":
            print("Näkemiin!")
        else:
            print("Tuntematon komento, yritä uudelleen.")