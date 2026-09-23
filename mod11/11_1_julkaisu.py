class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"{self.nimi}, kirjailija {self.kirjoittaja}, {self.sivumäärä} sivua")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi {self.nimi}, kirjoittaja {self.päätoimittaja}, sivumäärä {self.sivumäärä}")


lehti1 = Lehti("Aku Ankka", "Aki Hyppä")
kirja1 = Kirja("Hyyti no. 6", "Roosa Likson", 200)
lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()