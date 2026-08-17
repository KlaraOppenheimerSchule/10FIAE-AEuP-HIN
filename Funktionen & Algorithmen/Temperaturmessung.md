# Temperaturmessung

### Schwiergkeitsgrad: **

**Szenario**
Eine Wetterstation misst täglich die Temperatur (z.B. für eine Woche, 7 Werte, oder einen Monat, ca. 30 Werte). Die Werte sollen in einer Liste/einem Array gespeichert werden (Grad Celsius, Werte zwischen -10 und 40). Ziel: Schreibe für jede Auswertung eine eigene Funktion (Prinzip: eine Funktion = eine Aufgabe).

Beispieldaten: tagestemperaturen = [18, 22, 19, 25, 21, 17, 23]

**Aufgaben**
Hinweis: Nutze KEINE eingebauten Funktionen wie sum(), max(), min() – implementiere die Logik selbst mit Schleifen.


1. Schreiben Sie eine Funktion berechne_summe(werte), die die Summe aller Temperaturwerte einer Liste zurückgibt.

2. Schreiben Sie eine Funktion finde_hoechstwert(werte), die den höchsten Temperaturwert zurückgibt.

3. Schreiben Sie eine Funktion finde_niedrigstwert(werte), die den niedrigsten Temperaturwert zurückgibt.

4. Schreiben Sie eine Funktion berechne_durchschnitt(werte), die den Durchschnitt der Temperaturwerte berechnet (nutze ggf. deine berechne_summe-Funktion).

5. Schreiben Sie eine Funktion lineare_suche(werte, gesuchter_wert), die prüft, ob ein bestimmter Wert vorkommt und den Index zurückgibt, sonst -1.

6. Schreiben Sie eine Funktion lineare_suche_bereich(werte, untere_grenze, obere_grenze), die alle Indizes für Werte im Bereich zurückgibt (z.B. 18–22).

Jetzt werden die Temperaturen für mehrere Wochen gespeichert: eine Liste von Wochen-Listen, z.B.

wochen = [[18, 21, 19, 23, 17, 20, 22],
          [15, 16, 18, 20, 19, 17, 16],
          [22, 24, 23, 25, 21, 20, 19]]  # (3 Wochen à 7 Tage)

7. Schreiben Sie eine Funktion berechne_wochendurchschnitt(wochen, woche_index), die den Durchschnitt einer bestimmten Woche berechnet (Zugriff über zwei Indizes).

8. Schreiben Sie eine Funktion finde_beste_woche(wochen), die die Woche mit dem höchsten Durchschnitt findet und deren Index zurückgibt.

9. Schreiben Sie eine Funktion lineare_suche_2d(wochen, gesuchter_wert), die die gesamte 2D-Liste durchsucht (verschachtelte Schleife) und Woche+Tag (als Tupel/Position) zurückgibt, an der der Wert zum ersten Mal vorkommt, sonst None.
