class Klassenraum():
    def __init__(self, nummer, anzahlplaetze):
        self._nummer = nummer
        self._anzahlplaetze = anzahlplaetze

    def getNummer(self):
       return self._nummer
    
    def getPlaetze(self):
        return self._anzahlplaetze

class Seminarraum(Klassenraum):
    def __init__(self, nummer, anzahlplaetze):
        super().__init__(nummer, anzahlplaetze)
        self.__projektionsflaeche = None

    def setFlaeche(self,flaeche):
        self.__projektionsflaeche = flaeche

    def getFlaeche(self):
        return self.__projektionsflaeche


class Uebungsraum(Klassenraum):
    def __init__(self, nummer, anzahlplaetze):
        super().__init__(nummer, anzahlplaetze)
        self.__status = True
        self.__laptops = None
    
    def getLaptops(self):
        return self.__laptops
    
    def setLaptops(self,laptops):
        self.__laptops = laptops

    def getStatus(self):
        return self.__status
    
    def changeStatus(self):
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True
    
    
### Main ###
            
klassenraum1 = Klassenraum(108,32)
seminarraum1 = Seminarraum(107,6)
Uebungsraum1 = Uebungsraum(109,4)

print(klassenraum1.getNummer(), klassenraum1.getPlaetze())
print(seminarraum1.getNummer(), seminarraum1.getPlaetze(), seminarraum1.getFlaeche())
print(Uebungsraum1.getNummer(), Uebungsraum1.getPlaetze(), Uebungsraum1.getLaptops(), Uebungsraum1.getStatus())

Uebungsraum1.changeStatus()
print(Uebungsraum1.getNummer(), Uebungsraum1.getPlaetze(), Uebungsraum1.getLaptops(), Uebungsraum1.getStatus())

