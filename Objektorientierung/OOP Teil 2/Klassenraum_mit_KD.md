# Klassenraum

### Schwierigkeitsgrad: **

In der Schule gibt es mehrere Arten von Räumen. Der Auszug aus dem UML-Klassendiagramm zeigt die Klasse „Klassenraum“.

![Klassenraum](./KD%20Aufgaben%20OOP%20Teil%202/klassenraum.png)

1. Programmieren Sie die Klasse „Klassenraum“ wie im Diagramm zu sehen.
2. Erweitern Sie das Klassendiagramm um die Räume „Seminarraum“ und „Uebungsraum“. Beide erben von der Klasse „Klassenraum“. Folgende An-gaben liegen noch vor:
    - Der Seminarraum hat das private Attribut „Projektionsflaeche“. Für das Attribut liegt jeweils eine öffentliche Get- und Set-Methode vor. Bei der Instanziierung ist die Angabe der Projektionsflaeche nicht nötig.
    - Der Uebungsraum hat die privaten Attribute „Laptops“ (Anzahl der Lap-tops im Raum) und Status (ob der Raum belegt ist oder nicht). Für das Attribut liegen jeweils eine öffentliche Get- und Set-Methode vor. Bei der Instanziierung wird der Status auf True gesetzt.
    - Zusätzlich existiert noch die Methode „changeStatus“. Diese prüft den aktuellen Status (belegt = False oder frei = True) und ändert den Status. Ist der Raum belegt, so wird der Status nach der Ausführung der Methode auf frei gesetzt und umgekehrt. 
    - Zudem gibt es die Methode „getStatus“, die den aktuellen Status zurückgibt.
3. Setzen Sie Ihr UML-Klassendiagramm in Code um.
