# 1. Telefonbuch mit 5 Einträgen anlegen
telefonbuch = {
    "Anna": "0123-456789",
    "Ben": "0123-987654",
    "Clara": "0123-555555",
    "David": "0123-111111",
    "Emma": "0123-222222"
}

# Ausgabe des Telefonbuchs
print("Telefonbuch:")
for name, nummer in telefonbuch.items():
    print(f"  {name}: {nummer}")

# Nummer zu einem Namen suchen
print("\n--- Nummer suchen ---")
gesuchter_name = "Clara"
if gesuchter_name in telefonbuch:
    print(f"Nummer von {gesuchter_name}: {telefonbuch[gesuchter_name]}")
else:
    print(f"{gesuchter_name} nicht im Telefonbuch gefunden")

# 2. Neuen Eintrag hinzufügen mit Duplikat-Prüfung
print("\n--- Neuen Eintrag hinzufügen ---")
neuer_name = "Frank"
neue_nummer = "0123-333333"

if neuer_name in telefonbuch:
    print(f"Fehler: {neuer_name} existiert bereits!")
else:
    telefonbuch[neuer_name] = neue_nummer
    print(f"{neuer_name} hinzugefügt: {neue_nummer}")

# Versuch, einen existierenden Namen hinzuzufügen
print("\n--- Versuch, Duplikat hinzuzufügen ---")
duplikat_name = "Anna"
duplikat_nummer = "0123-999999"

if duplikat_name in telefonbuch:
    print(f"Fehler: {duplikat_name} existiert bereits!")
    print(f"Aktuelle Nummer: {telefonbuch[duplikat_name]}")
else:
    telefonbuch[duplikat_name] = duplikat_nummer

# Aktuelles Telefonbuch
print("\nAktuelles Telefonbuch:")
for name, nummer in telefonbuch.items():
    print(f"  {name}: {nummer}")

# 3. Nummer aktualisieren
print("\n--- Nummer aktualisieren ---")
zu_aendernder_name = "Ben"
neue_nummer_ben = "0123-777777"

if zu_aendernder_name in telefonbuch:
    alte_nummer = telefonbuch[zu_aendernder_name]
    telefonbuch[zu_aendernder_name] = neue_nummer_ben
    print(f"{zu_aendernder_name}:")
    print(f"  Alte Nummer: {alte_nummer}")
    print(f"  Neue Nummer: {neue_nummer_ben}")
else:
    print(f"Fehler: {zu_aendernder_name} nicht gefunden")

# Finales Telefonbuch
print("\nFinales Telefonbuch:")
for name, nummer in telefonbuch.items():
    print(f"  {name}: {nummer}")
