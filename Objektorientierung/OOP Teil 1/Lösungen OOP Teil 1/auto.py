class Auto:
    def __init__(self,modell,farbe):
        self.__modell = modell
        self.__farbe = farbe
      
    def getmodell(self):
        return self.__modell
    
    def getfarbe(self):
        return self.__farbe
    
    def fahre(self):
        print ("Brum, Brum")
        
    def geschwindigkeit(self,strecke : float,zeit :float):
        v = strecke / zeit
        return v

#car = Auto("Ford","blau")
#print(car.geschwindigkeit(20,5))
#car.fahre()
