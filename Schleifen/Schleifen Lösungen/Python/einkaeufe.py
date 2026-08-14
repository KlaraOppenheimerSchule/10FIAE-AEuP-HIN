gesamtpreis = 0.0

while True:
    produkt = int(input("Wurde ein Produkt gekauft? [0] Nein / [1] Ja: "))
    if produkt == 0:
        break
    else:
        preis = float(input("Wie viel kostet das Produkt? "))
        gesamtpreis += preis

print("Gesamtpreis:", round(gesamtpreis, 2), "Euro")

if gesamtpreis >= 20:
    print("Danke, dass Sie einen großen Einkauf getätigt haben!")
elif 0 < gesamtpreis <= 19:
    print("Danke, dass Sie einen kleinen Einkauf getätigt haben!")
elif gesamtpreis == 0:
    print("Schade, dass Sie nichts gekauft haben.")