# 1. Map mit Benutzer-IDs auf Namen
print("=== Schritt 1: Einfache Map (ID -> Name) ===")
benutzer_einfach = {
    1: "Anna",
    2: "Ben",
    3: "Clara",
    4: "David",
    5: "Emma"
}

print("Benutzerprofile (einfach):")
for user_id, name in benutzer_einfach.items():
    print(f"  ID {user_id}: {name}")

# 2. Erweiterte Map mit verschachtelten Daten
print("\n=== Schritt 2: Erweiterte Map (ID -> komplexe Daten) ===")
benutzer_erweitert = {
    1: {
        "name": "Anna",
        "alter": 25,
        "email": "anna@example.com"
    },
    2: {
        "name": "Ben",
        "alter": 30,
        "email": "ben@example.com"
    },
    3: {
        "name": "Clara",
        "alter": 28,
        "email": "clara@example.com"
    },
    4: {
        "name": "David",
        "alter": 35,
        "email": "david@example.com"
    },
    5: {
        "name": "Emma",
        "alter": 22,
        "email": "emma@example.com"
    }
}


# Neuen Benutzer hinzufügen
print("\n=== Neuen Benutzer hinzufügen ===")
neue_id = 6
benutzer_erweitert[neue_id] = {
    "name": "Frank",
    "alter": 32,
    "email": "frank@example.com"
}

profil = benutzer_erweitert[neue_id]
print(f"Neuer Benutzer (ID {neue_id}):")
print(f"  Name: {profil['name']}")
print(f"  Alter: {profil['alter']}")
print(f"  E-Mail: {profil['email']}")

# E-Mail eines Benutzers aktualisieren
print("\n=== E-Mail aktualisieren ===")
aenderungs_id = 2
alte_email = benutzer_erweitert[aenderungs_id]['email']
benutzer_erweitert[aenderungs_id]['email'] = "ben.neu@example.com"
neue_email = benutzer_erweitert[aenderungs_id]['email']

print(f"Benutzer ID {aenderungs_id} ({benutzer_erweitert[aenderungs_id]['name']}):")
print(f"  Alte E-Mail: {alte_email}")
print(f"  Neue E-Mail: {neue_email}")

