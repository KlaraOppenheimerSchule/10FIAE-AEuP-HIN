# Mitarbeiter und Admin

### Schwierigkeitsgrad: **

1. Schreiben Sie eine Klasse „Mitarbeiter“, die die geschützten Attribute Name und Abteilungsnummer hat. Beide Attribute sind Instanzvariablen. Es ist möglich, dass nur der Mitarbeitername angegeben wird ohne eine Abtei-lungsnummer, jedoch nie eine Abteilungsnummer ohne Mitarbeiternamen. Für den Mitarbeiternamen gibt es eine öffentliche Get-Methode und für die Abteilungsnummer eine öffentliche Get-und Set-Methode.

2. Implementieren Sie nun das private Attribut „ticketsbearbeiten“ vom Typ einer Liste. Implementieren Sie zudem die öffentliche Methode „Support“, welche ein mehrdimensionales Array folgender Form übergeben bekommt:
                Beispiel:
                tickets = [
                [1,1,1138],
                [2,3, 2768],
                [3,2,3489]
                ]
tickets[x][0] = Ticketnummer, tickets[x][1] = Supportlevel, tickets[x][2] = Supportcode
	
    Die Methode “Support” durchläuft dabei das übergebene Array und prüft das Supportlevel. Ist das Supportlevel kleiner als 2, so wird das Ticket der Liste „ticketsbearbeiten“ hinzugefügt. 
        
    Bitte beachten: Die Begriffe Array und Liste sind im Kontext der jeweiligen Programmiersprache zu verstehen! Finden Sie die jeweils passenden Daten-typen für Ihre Programmiersprache.

3. Schreiben Sie nun die Klasse „Admin“, die von der Klasse Mitarbeiter erbt. Überschreiben Sie die Methode „Support“, sodass nun alle Tickets mit dem Supportlevel über 1 der Liste „ticketsbearbeiten“ hinzugefügt werden.
