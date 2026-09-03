tuumat = float(input("Anna tuumat: "))

while tuumat >= 0:
    sentit = tuumat * 2.54  # koska 1 tuuma = 2,54 cm
    print(f"{tuumat} tuumaa on {sentit} cm.")
    tuumat = float(input("Anna tuumat: "))

# Jos käyttäjä syötti negatiivisen luvun
print("Annoit negatiivisen luvun. Ohjelma lopettaa.")
