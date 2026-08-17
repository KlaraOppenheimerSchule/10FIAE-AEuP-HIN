# 1. Dictionary mit 5 Produkten und Preisen anlegen
preiskatalog = {
    "Laptop": 899.99,
    "Monitor": 299.99,
    "Tastatur": 79.99,
    "Maus": 29.99,
    "Kopfhörer": 149.99
}

# Preis eines bestimmten Produkts ausgeben
print("Preiskatalog:")
for produkt, preis in preiskatalog.items():
    print(f"  {produkt}: {preis}€")

print(f"\nPreis von 'Laptop': {preiskatalog['Laptop']}€")

# 2. Neues Produkt hinzufügen
print("\n--- Neues Produkt hinzufügen ---")
preiskatalog["Webcam"] = 89.99
print(f"Webcam hinzugefügt: {preiskatalog['Webcam']}€")

# Bestehenden Preis ändern
print("\n--- Preis ändern ---")
print(f"Alter Preis Monitor: {preiskatalog['Monitor']}€")
preiskatalog["Monitor"] = 349.99
print(f"Neuer Preis Monitor: {preiskatalog['Monitor']}€")

# Produkt entfernen
print("\n--- Produkt entfernen ---")
del preiskatalog["Maus"]
print("Maus wurde entfernt")

# Aktueller Katalog
print("\nAktueller Katalog:")
for produkt, preis in preiskatalog.items():
    print(f"  {produkt}: {preis}€")

# 3. Gesamtwert des Katalogs berechnen
print("\n--- Gesamtwert des Katalogs ---")
gesamtwert = sum(preiskatalog.values())
print(f"Gesamtwert: {gesamtwert}€")

# Teuerstes Produkt finden
print("\n--- Teuerstes Produkt ---")
teuerstes_produkt = max(preiskatalog, key=preiskatalog.get)
teuerstes_preis = preiskatalog[teuerstes_produkt]
print(f"{teuerstes_produkt}: {teuerstes_preis}€")

# Günstigstes Produkt finden
print("\n--- Günstigstes Produkt ---")
guenstigstes_produkt = min(preiskatalog, key=preiskatalog.get)
guenstigstes_preis = preiskatalog[guenstigstes_produkt]
print(f"{guenstigstes_produkt}: {guenstigstes_preis}€")
