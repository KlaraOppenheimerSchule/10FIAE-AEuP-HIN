# Fitnesstracker

### Schwierigkeitsgrad: *

**Szenario**

Szenario: Ein Fitnesstracker speichert die Anzahl der Schritte pro Wochentag als Key-Value-Paare (Dictionary), 

z.B.
schritte = {"Montag": 8500, "Dienstag": 12000, "Mittwoch": 6000,
            "Donnerstag": 9500, "Freitag": 11000, "Samstag": 15000, "Sonntag": 4000}


**Aufgaben**
1. Schreiben Sie eine Funktion berechne_summe(schritte), die die Gesamtzahl aller Schritte berechnet (Schleife über .values(), ohne sum()).

2. Schreiben Sie eine Funktion finde_hoechsten_tag(schritte), die den Tag mit den meisten Schritten UND die Anzahl zurückgibt (ohne max()).

3. Schreiben Sie eine Funktion finde_niedrigsten_tag(schritte), die den Tag mit den wenigsten Schritten UND die Anzahl zurückgibt (ohne min()).

4. Schreiben Sie eine Funktion zaehle_tage_ueber_grenze(schritte, grenzwert), die zählt, an wie vielen Tagen die Schrittzahl über einem bestimmten Grenzwert lag (z.B. 10000).

5. Schreiben Sie eine Funktion lineare_suche_bereich(schritte, min_wert, max_wert), die alle Tage zurückgibt (als Liste), deren Schrittzahl zwischen min_wert und max_wert liegt.

6. Erweiterung auf mehrere Wochen: Nun gibt es ein verschachteltes Dictionary für mehrere Wochen, z.B.
wochen_schritte = {"Woche1": {"Montag": 8500, ...}, "Woche2": {"Montag": 9000, ...}}

7. Schreibe eine Funktion vergleiche_wochen(wochen_schritte), die die Gesamtsumme jeder Woche berechnet und die Woche mit der höchsten Gesamtsumme zurückgibt.
