# Beispieldaten
schritte = {"Montag": 8500, "Dienstag": 12000, "Mittwoch": 6000,
            "Donnerstag": 9500, "Freitag": 11000, "Samstag": 15000, "Sonntag": 4000}


# 1. Summe aller Schritte berechnen
def berechne_summe(schritte):
    summe = 0
    for wert in schritte.values():
        summe += wert
    return summe


# 2. Tag mit den meisten Schritten finden
def finde_hoechsten_tag(schritte):
    hoechster_tag = None
    hoechste_anzahl = None

    for tag, anzahl in schritte.items():
        if hoechste_anzahl is None or anzahl > hoechste_anzahl:
            hoechster_tag = tag
            hoechste_anzahl = anzahl

    return hoechster_tag, hoechste_anzahl


# 3. Tag mit den wenigsten Schritten finden
def finde_niedrigsten_tag(schritte):
    niedrigster_tag = None
    niedrigste_anzahl = None

    for tag, anzahl in schritte.items():
        if niedrigste_anzahl is None or anzahl < niedrigste_anzahl:
            niedrigster_tag = tag
            niedrigste_anzahl = anzahl

    return niedrigster_tag, niedrigste_anzahl


# 4. Tage über einem Grenzwert zählen
def zaehle_tage_ueber_grenze(schritte, grenzwert):
    anzahl_tage = 0
    for anzahl in schritte.values():
        if anzahl > grenzwert:
            anzahl_tage += 1
    return anzahl_tage


# 5. Lineare Suche im Bereich (alle passenden Tage)
def lineare_suche_bereich(schritte, min_wert, max_wert):
    gefundene_tage = []
    for tag, anzahl in schritte.items():
        if min_wert <= anzahl <= max_wert:
            gefundene_tage.append(tag)
    return gefundene_tage


# 6. Mehrwochen-Daten (verschachteltes Dictionary)
wochen_schritte = {
    "Woche1": {"Montag": 8500, "Dienstag": 12000, "Mittwoch": 6000,
               "Donnerstag": 9500, "Freitag": 11000, "Samstag": 15000, "Sonntag": 4000},
    "Woche2": {"Montag": 9000, "Dienstag": 10500, "Mittwoch": 7000,
               "Donnerstag": 8000, "Freitag": 13000, "Samstag": 14000, "Sonntag": 5000},
    "Woche3": {"Montag": 7500, "Dienstag": 11500, "Mittwoch": 9000,
               "Donnerstag": 10000, "Freitag": 12000, "Samstag": 16000, "Sonntag": 6000}
}


# 7. Wochen vergleichen (nutzt berechne_summe)
def vergleiche_wochen(wochen_schritte):
    beste_woche = None
    beste_summe = None

    for woche, tage_daten in wochen_schritte.items():
        summe = berechne_summe(tage_daten)
        if beste_summe is None or summe > beste_summe:
            beste_woche = woche
            beste_summe = summe

    return beste_woche, beste_summe


# --- Testausgaben ---
if __name__ == "__main__":
    print("=== Schrittdaten (eine Woche) ===")
    for tag, anzahl in schritte.items():
        print(f"  {tag}: {anzahl} Schritte")

    print("\nGesamtsumme:", berechne_summe(schritte))

    tag, anzahl = finde_hoechsten_tag(schritte)
    print(f"Höchster Tag: {tag} mit {anzahl} Schritten")

    tag, anzahl = finde_niedrigsten_tag(schritte)
    print(f"Niedrigster Tag: {tag} mit {anzahl} Schritten")

    print("\n--- Tage über Grenzwert 10000 ---")
    print("Anzahl:", zaehle_tage_ueber_grenze(schritte, 10000))

    print("\n--- Lineare Suche im Bereich 8000-12000 ---")
    print("Tage:", lineare_suche_bereich(schritte, 8000, 12000))

    print("\n=== Mehrwochen-Vergleich ===")
    for woche, tage_daten in wochen_schritte.items():
        print(f"{woche}: Gesamtsumme = {berechne_summe(tage_daten)}")

    beste_woche, beste_summe = vergleiche_wochen(wochen_schritte)
    print(f"\nBeste Woche: {beste_woche} mit {beste_summe} Schritten insgesamt")
