class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def kerros_ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen = self.nykyinen + 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen = self.nykyinen - 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin:
            kerros = self.alin
        elif kerros > self.ylin:
            kerros = self.ylin

        while self.nykyinen < kerros:
            self.kerros_ylos()
        while self.nykyinen > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissin_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissin_maara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohde):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohde)

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin)


h = Hissi(1, 10)
h.siirry_kerrokseen(6)
h.siirry_kerrokseen(1)

talo = Talo(1, 10, 2)
talo.aja_hissia(1, 5)
talo.palohalytys()