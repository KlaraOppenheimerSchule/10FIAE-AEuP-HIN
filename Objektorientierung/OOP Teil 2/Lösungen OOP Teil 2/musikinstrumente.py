'''Lösung a)
Die Klasse Musikinstrument ist eine abstrakte Klasse. Diese besondere Klasse kann nicht instanziiert werden und kann zudem abstrakte Methoden enthalten, 
welche eine Methodensignatur besitzen jedoch keine Programmierung. Diese Methoden werden dann in den zu erbenden Klassen implementiert. 
Dies ist der Fall bei der Methode getDaten(), da sie eine abstrakte Methode ist und auch so gekennzeichnet ist. Diese wird dann in den zu 
erbenden Klas-sen implementiert.
'''


### Polymorphie
'''Die abstrakte Methode getDaten() wird in die erbenden 
Klassen implementiert. Hierbei werden Sie ausprogrammiert. 
Die Methoden werden somit überschrieben. 
'''

from abc import ABC, abstractmethod

### abstrakte Klasse ###

class Musikinstrument(ABC):
    def __init__(self,modell,hersteller,preis):
        self._modell = modell
        self._hersteller = hersteller
        self._preis = preis
    
    def getModell(self):
        return self._modell
    
    def setModell(self,modell):
        self._modell = modell
    
    def getHersteller(self):
        return self._hersteller
    
    def setHersteller(self,hersteller):
        self._hersteller = hersteller
    
    def getPreis(self):
        return self._preis
    
    def setPreis(self,preis):
        self._preis = preis
    
    @abstractmethod
    def getDaten(self):
        pass

### Gitarre ###
    
class Gitarre(Musikinstrument):
    def __init__(self,modell,hersteller,preis,groesse):
        super().__init__(modell,hersteller,preis)
        self._groesse = groesse
    
    def getGroesse(self):
        return self._groesse
    
    def setGroesse(self,groesse):
        self._groesse = groesse
    
    def getDaten(self):
        daten = "Die Gitarre ist vom Herstel-ler",self._hersteller,", Modell",self._modell,"und hat eine Größe von ",self._groesse,".\n Sie kostet",self._preis,"Euro"
        return daten

### Saxophon ##

class Saxophon(Musikinstrument):
    def __init__(self, modell, hersteller, preis, stimmung):
        super().__init__(modell, hersteller, preis)
        self._stimmmung = stimmung

    def getStimmung(self):
        return self._stimmmung
    
    def setStimmung(self,stimmung):
        self._stimmmung = stimmung
    
    def getDaten(self):
        daten = "Hier steht anderer Text",self._hersteller
        return daten

gitarre = Gitarre("Spass","Yamaha",33.00,20)
saxophon = Saxophon("txt","Selma","300.00","Es")

print(gitarre.getDaten())
print(saxophon.getDaten())
