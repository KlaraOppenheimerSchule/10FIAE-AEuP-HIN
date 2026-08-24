from abc import ABC, abstractmethod

## Abstrakte Klasse Server ###
class Server(ABC):
    def __init__(self,name,hauptspeicher):
        self._name = name
        self._hauptspeicher = hauptspeicher

    def getName(self):
        return self._name
    
    def getSpeicher(self):
        return self._hauptspeicher

class Proxyserver(Server):
    def __init__(self, name, preis, hauptspeicher,protokoll):
        super().__init__(name, preis, hauptspeicher)
        self._protokoll = protokoll
    
    def getProtokoll(self):
        return self._protokoll
    


class Datenbankserver(Server):
    def __init__(self, name, preis, hauptspeicher,dbms):
        super().__init__(name, preis, hauptspeicher)
        self._dbms = dbms
    
    def getDbms(self):
        return self._dbms
    
    def setSpeicher(self,speicher):
        self._hauptspeicher = speicher
