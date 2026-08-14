# Muss nicht ins AD
from random import *

# Ab hier in AD
ratezahl = randint(1,100)
hit = False
i = 0

while i < 7 and hit == False:
    raten = int(input("Bitte Tipp abgeben: ")) 
    if raten < ratezahl:
        print("Deine geratene Zahl ist zu klein!")
        print("Du hast noch ", 6-i, "Versuche")
        raten = int(input("Bitte Tipp abgeben: "))
        i = i + 1
        
    elif raten > ratezahl:
        print("Deine geratene Zahl ist zu groß!")
        print("Du hast noch ", 6-i, "Versuche")
        raten = int(input("Bitte Tipp abgeben: "))
        i = i + 1
    
    elif raten == ratezahl:
        hit = True
    
if hit == False:
    print("Schade – verloren. Einfach nochmals probieren!")
  

else:
    print("Gewonnen! Die geheime Zahl ist nicht mehr geheim")

          