alter = int(input("Geben Sie das Alter ein: "))
anzahl_personen = int(input("Geben Sie die Anzahl an Personen ein: "))
ist_vip = int(input("Sind Sie VIP-Kunde? (0) = Nein, (1) = Ja : "))


if alter < 5:
    preis = 0
elif 5 <= alter <= 12:
    preis = 10
elif 13 <= alter <= 17:
    preis = 15
elif 18 <= alter <= 64:
    preis = 20
else:  # Alter 65 oder älter
    preis = 12

# Rabatt für VIP
if ist_vip == 1:
    preis *= 0.5  # 50% Rabatt

# Familienbonus: zusätzlicher Rabatt von 10% für Gruppen über 3 Personen
if anzahl_personen > 3:
    preis *= 0.9  # 10% Rabatt

print(round(preis, 2))  # Preis auf 2 Dezimalstellen runden

