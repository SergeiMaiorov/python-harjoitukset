class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka = self.matka + (self.nopeus * tunnit)

auto = Auto("ABC-123", 142)
print(f"Auto: {auto.rekisteritunnus}, Huippunopeus: {auto.huippunopeus}, Nopeus: {auto.nopeus}, Matka: {auto.matka}")

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Nopeus nyt: {auto.nopeus}")

auto.kiihdyta(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus}")