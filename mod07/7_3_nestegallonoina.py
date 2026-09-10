def gallona_litroiksi(gallonat):
    return gallonat * 3.785

maara = float(input("Anna bensiinin määrä gallonoina: "))

while maara >= 0:
    litrat = gallona_litroiksi(maara)
    print(f"{maara} gallonaa on {litrat} litraa.")
    maara = float(input("Anna bensiinin määrä gallonoina: "))