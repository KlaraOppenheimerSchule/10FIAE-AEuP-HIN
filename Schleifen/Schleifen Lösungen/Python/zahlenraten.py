from random import *

i = 1
raten = int(input("Bitte Tipp abgeben: "))
ratezahl = randint(1,100)
hit = False

while i < 7 and hit == False: 
    if raten < ratezahl:
        print("Deine geratene Zahl ist zu klein!")
        print("Du hast noch ", 7-i, "Versuche")
        raten = int(input("Bitte Tipp abgeben: "))
        i = i + 1
        
    elif raten > ratezahl:
        print("Deine geratene Zahl ist zu groß!")
        print("Du hast noch ", 7-i, "Versuche")
        raten = int(input("Bitte Tipp abgeben: "))
        i = i + 1
    elif raten == ratezahl:
        hit = True
    
if hit == False:
    print("Schade – verloren. Einfach nochmals probieren!")
    print("Ende des Spiels. Die Zahl lautete: ", ratezahl)

else:
    print("Gewonnen! Die geheime Zahl ist nicht mehr geheim")
    print("Du hast ", i, "Versuche benötigt")
          