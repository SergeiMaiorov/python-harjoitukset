## Pyydä suorakulmion kannan ja korkeus
korkeus = float(input("Anna suorakulmion korkeus: "))
leveys = float(input("Anna suorakulmion leveys: "))


## lasken suorakulmion piirin
## kaava on 2 * (korkeus  * leveys )
piiri = 2 * (korkeus * leveys)


## lasken suorakulmion kannan pinta-alan
## kaava on kanta * korkeus
pinta_ala = korkeus * leveys


## tulosta suorakulmion piirin
print(f"Suorakulmion piirin on {piiri}")


## tulosta suorakulmion  pinta-alan
print(f"Suorakulmion pinta-ala on {pinta_ala}")
