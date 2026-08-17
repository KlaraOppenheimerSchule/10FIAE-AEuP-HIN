# 1. 2D-Struktur für 3 Produkte über 4 Monate anlegen
# Zeilen = Produkte, Spalten = Monate
verkaufszahlen = [
    [150, 200, 180, 220],  # Produkt 1
    [300, 280, 320, 350],  # Produkt 2
    [100, 120, 110, 140]   # Produkt 3
]

produkte = ["Produkt 1", "Produkt 2", "Produkt 3"]
monate = ["Januar", "Februar", "März", "April"]

# Ausgabe der Struktur
print("Verkaufszahlen (Produkt x Monat):")
print("         ", end="")
for monat in monate:
    print(f"{monat:<12}", end="")
print()

for i in range(3):
    print(f"{produkte[i]:<9}", end="")
    for j in range(4):
        print(f"{verkaufszahlen[i][j]:<12}", end="")
    print()

# 2. Summe der Verkäufe pro Produkt
print("\n--- Summe pro Produkt ---")
for i in range(3):
    summe_produkt = sum(verkaufszahlen[i])
    print(f"{produkte[i]}: {summe_produkt} Verkäufe")

# Summe der Verkäufe pro Monat
print("\n--- Summe pro Monat ---")
for j in range(4):
    summe_monat = 0
    for i in range(3):
        summe_monat += verkaufszahlen[i][j]
    print(f"{monate[j]}: {summe_monat} Verkäufe")

# 3. Monat mit höchstem Gesamtumsatz
print("\n--- Monat mit höchstem Gesamtumsatz ---")
max_umsatz = 0
bester_monat = ""

for j in range(4):
    summe_monat = 0
    for i in range(3):
        summe_monat += verkaufszahlen[i][j]
    
    if summe_monat > max_umsatz:
        max_umsatz = summe_monat
        bester_monat = monate[j]

print(f"{bester_monat}: {max_umsatz} Verkäufe")

# Produkt mit wenigsten Verkäufen insgesamt
print("\n--- Produkt mit wenigsten Verkäufen ---")
min_verkaufe = sum(verkaufszahlen[0])
schlechtestes_produkt = ""

for i in range(3):
    summe_produkt = sum(verkaufszahlen[i])
    if summe_produkt < min_verkaufe:
        min_verkaufe = summe_produkt
        schlechtestes_produkt = produkte[i]

print(f"{schlechtestes_produkt}: {min_verkaufe} Verkäufe")
