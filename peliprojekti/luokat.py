#Luokat "Avaruuden reuna" pelista
##Luokkien (Huone ja Pelaaja) yhdistäminen perustuvat Github-käyttäjä AvaHeinonen koodiin osoitteessa https://github.com/AvaHeinonen/huoneGame/blob/main/huone_game.py

class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

class Huone:
    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.exits = {}
        self.esine = None

    def add_exit(self, suunta, huone):
        self.exits[suunta] = huone

    def has_exit(self, suunta):
        return suunta in self.exits

    def get_next_huone(self, suunta):
        return self.exits.get(suunta)

class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.reppu = []

    def liiku(self, suunta):
        if self.sijainti.has_exit(suunta):
            self.sijainti = self.sijainti.get_next_huone(suunta)
            print(f"Menit suuntaan: {suunta}")
        else:
            print("Et voi mennä sinne")

    def keraa_esine(self):
        if self.sijainti.esine:
            tavara = self.sijainti.esine
            self.reppu.append(tavara)
            print(f"Löysit esineen: {tavara.nimi}")
            self.sijainti.esine = None
        else:
            print("Täällä ei ole mitään kerättävää!")