from abc import ABC, abstractmethod

class Datenbank():
    def __init__(self, dbname, user, password, ip, port):
        self.__dbname = dbname
        self.__user = user
        self.__password = password
        self.__ip = ip
        self.__port = port

    def getDBName(self):
        return self.__dbname        

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
    def __init__(self, name, hauptspeicher,dbms):
        super().__init__(name, hauptspeicher)
        self._dbms = dbms
        self._db = []
        self._ip = "127.0.0.1"
        self._port = 3306

    
    def getDbms(self):
        return self._dbms
    
    def setSpeicher(self,speicher):
        self._hauptspeicher = speicher
    
    def createDB(self, dbname, user, password):
        self._db.append(Datenbank(dbname,user,password,self._ip,self._port))

    def getDBs(self):
        tempdb = []
        for element in self._db:
            tempdb.append(element.getDBName())
        return tempdb
    


test = Datenbankserver("test",1000,"SQL")

test.createDB("kosidas","root","1234")
test.createDB("luna","root","1234")
test.createDB("nordwind","root","1234")

print(test.getDBs())
