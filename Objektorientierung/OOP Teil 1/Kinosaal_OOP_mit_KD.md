# Kinosaal (Objektorientiert)


Grundlage der Aufgabe ist die Einführungsaufgabe zu komplexen Datentypen "Kinosaal".


### Schwierigkeitsgrad: **


1. Bauen Sie die Aufgabe Kinosaal so um, dass diese objektorientiert ist. Dazu haben Sie folgende Angaben:
    - Jeder Kinosaal besitzt die Eigenschaften Raumnummer und Anzahl_Reihen und Sitze_pro_Reihe, welche vor dem Zugriff von außen geschützt sein sollen.
    - Raumnummer, Anzahl_Reihen und Sitze_pro_Reihe sind Instanzvariablen und sind bei der Objekterzeugung notwendig.
    - Jeder einzelne Sitz muss für eine spätere Reservierung / Buchung gespeichert werden. Realisieren Sie dies in der Klasse (nur Attribut mit sinnvollem Datentyp und Sichtbarkeit). Beachten Sie, dass für jeden Saal eine andere Anzahl an Sitzen verfügbar ist.
    - Um zu erfahren, welche Raumnummer und Anzahl_Sitze des Kinosaals sind, sind hierfür jeweils eine Get-Methode erforderlich. (Achtung: die Get-Methode für Anzahl_Sitze liefert die Summe aller Sitze im Saal zurück)
   
2. Schreiben Sie in einer objektorientierten Programmiersprache Ihrer Wahl ei-ne Methode, welche die Reservierung eines bestimmten Sitzplatzes ermöglicht. 

3. Die Reservierung bestimmter Sitze ist sicher für Kinobesucher sehr angenehm. Aber zusätzlich soll es eine Methode geben, die irgendeinen Sitz, welcher noch frei ist, bucht. Schreiben Sie eine passende Methode, die die-ser Anforderung gerecht wird.

4. Nun wird noch eine Methode benötigt, bei der der Kunde eine beliebige Anzahl an Sitzen buchen kann. Folgendes ist dabei zu beachten: 
- Die Sitze müssen nicht zusammenhängend sein. Jeder freie Sitzplatz kann gebucht werden. 
- Eine Angabe von genauen Sitznummern (bzw. Reihe und Sitz) durch den Kunden ist nicht notwendig. 
- Die Buchung ist eine zusammenhängende Buchung. Sollte nur ein Platz zu wenig frei sein, so ist die komplette Buchung nicht durchzuführen. Bei-spiel: Ein Kunde will 3 Sitze buchen, nur 2 sind frei. So wird keiner gebucht.


3. Zeichnen Sie die Klasse "Kinosaal" als UML-Klasse.



