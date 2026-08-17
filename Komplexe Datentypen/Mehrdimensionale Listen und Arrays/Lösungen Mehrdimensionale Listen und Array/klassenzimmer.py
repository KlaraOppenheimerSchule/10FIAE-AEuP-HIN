# 1. Sitzplan-Raster anlegen (4x5)
sitzplan = [
    ["frei", "frei", "frei", "frei", "frei"],
    ["frei", "frei", "frei", "frei", "frei"],
    ["frei", "frei", "frei", "frei", "frei"],
    ["frei", "frei", "frei", "frei", "frei"]
]

# 2. Schülernamen zuweisen
sitzplan[0][0] = "Anna"
sitzplan[0][2] = "Ben"
sitzplan[1][1] = "Clara"
sitzplan[2][3] = "David"
sitzplan[3][4] = "Emma"

# Sitzplan tabellarisch ausgeben
print("Sitzplan:")
print("  ", end="")
for spalte in range(5):
    print(f"Spalte {spalte}  ", end="")
print()

for zeile in range(4):
    print(f"Zeile {zeile}: ", end="")
    for spalte in range(5):
        print(f"{sitzplan[zeile][spalte]:<12}", end="")
    print()

# 3. Alle freien Plätze finden
print("\nFreie Plätze:")
for zeile in range(4):
    for spalte in range(5):
        if sitzplan[zeile][spalte] == "frei":
            print(f"  Zeile {zeile}, Spalte {spalte}")

# 4. Zwei Schüler tauschen (z.B. Anna und Clara)
print("\n--- Tausch: Anna (0,0) <-> Clara (1,1) ---")
sitzplan[0][0], sitzplan[1][1] = sitzplan[1][1], sitzplan[0][0]

print("Sitzplan nach Tausch:")
print("  ", end="")
for spalte in range(5):
    print(f"Spalte {spalte}  ", end="")
print()

for zeile in range(4):
    print(f"Zeile {zeile}: ", end="")
    for spalte in range(5):
        print(f"{sitzplan[zeile][spalte]:<12}", end="")
    print()
