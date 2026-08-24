
class Mitarbeiter():
    def __init__(self, *args ):
        if len(args) > 2:
            print("Zu viele Argumente")
        elif len(args) == 2:
            if isinstance(args[0], str ):
                self._name = args[0]
                self._abteilungnr = args[1]
            else:
                self._name = args[1]
                self._abteilungnr = args[0]
        else:
            if isinstance(args[0], str):
                self._name = args[0]
                self._abteilungnr = None
            else:
                print("Name angeben")
        self._ticketsbearbeiten = []

    
    def getName(self):
        return self._name
    
    def getAbteilung(self):
        return self._abteilungnr

    def setAbteilumg(self, abteilungnr):
        self._abteilungnr = abteilungnr

    def support(self, tickets):
        i = 0
        while i < len(tickets):
            if tickets[i][1] < 2:
                self._ticketsbearbeiten.append(tickets[i])
            i+=1
    
    def getTickets(self):
        return self._ticketsbearbeiten
