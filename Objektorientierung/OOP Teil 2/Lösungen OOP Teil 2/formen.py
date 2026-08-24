
from abc import ABC, abstractmethod
import math

## Interface Berechnung
class Berechnung(ABC):
    @abstractmethod
    def berechneFlaeche(self):
        pass
    @abstractmethod
    def berechneUmfang(self):
        pass


class Rechteck(Berechnung):
    
    def __init__(self):
        self.__laenge = 0
        self.__breite = 0

    def getLaenge(self):
        return self.__laenge
    
    def getBreite(self):
        return self.__breite
    
    def setLaenge(self,laenge):
        self.__laenge = laenge

    def setBreite(self, breite):
        self.__breite = breite
    
    def berechneUmfang(self):
        umfang = (self.__breite+self.__laenge)*2
        return umfang
    
    def berechneFlaeche(self):
        flaeche = self.__breite*self.__laenge
        return flaeche


class Kreis(Berechnung):
    def __init__(self):
        self.__radius = 0
    
    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius):
        self.__radius = radius
    
    def berechneFlaeche(self):
        flaeche = math.pi*self.__radius*self.__radius
        return flaeche
    
    def berechneUmfang(self):
        umfang = math.pi*2*self.__radius
        return umfang


kreis = Kreis()
kreis.setRadius(3.0)

rechteck = Rechteck()
rechteck.setBreite(3)
rechteck.setLaenge(3)

print(kreis.berechneFlaeche())
print(kreis.berechneUmfang())

print(rechteck.berechneUmfang())
print(rechteck.berechneFlaeche())
