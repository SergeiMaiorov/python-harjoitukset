import random 

class Auto:
    def __init__(self, rekistertunnus, hippunnopeus):
        self.rekistertunnus = rekistertunnus
        self.hippunnopeus = hippunnopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        if self.nopeus + muutos <= 0:
            self.nopeus = 0
        elif self.nopeus + muutos >= self.hippunnopeus:
            self.nopeus = self.hippunnopeus
        else:
            self.nopeus += muutos

    def kuljeta(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + tunnit * self.nopeus


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kuljeta(1)
            
    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"{auto.rekistertunnus} {auto.nopeus} {auto.kuljettu_matka}") 
            
    def kilpailu_ohi(self):
        ohi = False
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                ohi = True
                break
        return ohi


autot = []
for i in range(0, 10):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))
    
ralli = Kilpailu("Suuri Ralli", 8000, autot)


hours = 0
while not ralli.kilpailu_ohi():
    ralli.tunti_kuluu()
    hours += 1  
    if hours % 10 == 0:
        ralli.tulosta_tilanne()

ralli.tulosta_tilanne()




