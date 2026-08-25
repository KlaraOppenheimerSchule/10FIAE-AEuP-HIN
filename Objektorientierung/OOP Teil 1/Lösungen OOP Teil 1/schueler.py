class Schueler:
    def __init__(self,name,mail,klasse, alter):
        self.__name = name
        self.__mail = mail
        self.__klasse = klasse
        self.__alter = alter
        self.__feacher = []
         
    def getName(self):
        return self.__name
    
    def getMail(self):
        return self.__mail
    
    def getKlasse(self):
        return self.__klasse
    
    def getAlter(self):
        return self.__alter
    
    def setMail(self,mail):
        self.__mail = mail
        
    def setKlasse(self,klasse):
        self.__klasse = klasse
    
    def pruefeVolljaehrig(self):
        if self.__alter >= 18:
            return True
        else:
            return False
    
    def addFach(self,fach):
        duplicate = False
        x = 0
        while x < len(self.__feacher):
            if self.__feacher[x] == fach:
                duplicate = True
            x+=1
        if duplicate == False:
            self.__feacher.append(fach)
            print("Fach hinzuegfügt")
        else:
            print("Fach schon gespeichert")

    def deleteFach(self,fach):
        self.__feacher.remove(fach)
        print("Fach entfernt")
        
    def getFaecher(self):
        for x in self.__feacher:
            print(x)





stefan = Schueler("Stefan","test@test","10FI4",18)


#print(stefan.pruefeVolljaehrig())
stefan.addFach("Musik")
stefan.addFach("AEuP")
stefan.addFach("Test")
stefan.addFach("Musik")
stefan.getFaecher()
stefan.deleteFach("Musik")
stefan.getFaecher()
