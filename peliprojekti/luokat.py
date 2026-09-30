#Luokat "Avaruuden reuna" pelista

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

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def has_exit(self, direction):
        return direction in self.exits

    def get_next_room(self, direction):
        return self.exits.get(direction)

class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.reppu = []

    def liiku(self, suunta):
        if self.sijainti.has_exit(suunta):
            self.sijainti = self.sijainti.get_next_room(suunta)
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