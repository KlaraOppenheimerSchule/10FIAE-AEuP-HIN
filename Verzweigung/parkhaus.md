# 


# Parkhaus


### Schwiergkeit: ***


Es soll ein Programm für eine Statusanzeige eines Parkhauses entwickelt werden. Das Parkhaus hat insgesamt 500 Stellplätze. Die belegten Stellplätze werden automatisch ermittelt.Gegeben ist folgende Entscheidungstabelle für die Statusanzeige:


| Bedingungen | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Auslastung > 95% | Ja | Ja | Ja | Ja | Nein | Nein | Nein | Nein |
| Ein - oder Ausfahrt blockiert | Ja | Ja | Nein | Nein | Ja | Ja | Nein | Nein |
| Für Veranstaltung angemietet | Ja | Nein | Ja | Nein | Ja | Nein | ja | Nein |
| Aktion |  |  |  |  |  |  |  |  |
| Ausgabe "Parkhaus belegt" |  |  |  | x |  |  |  |  |
| Ausgabe "Parkhaus frei" |  |  |  |  |  |  |  | x |
| Ausgabe "Parkhaus gesperrt" | x | x | x |  | x | x | x |  |



Schreiben Sie ein Programm, das je nach Bedingung die korrekte Ausgabe erzeugt.

## Was sind Entscheidungstabellen und wie funktionieren sie?


[https://de.wikipedia.org/wiki/Entscheidungstabelle](https://de.wikipedia.org/wiki/Entscheidungstabelle)  
[https://t2informatik.de/wissen-kompakt/entscheidungstabelle/](https://t2informatik.de/wissen-kompakt/entscheidungstabelle/)


