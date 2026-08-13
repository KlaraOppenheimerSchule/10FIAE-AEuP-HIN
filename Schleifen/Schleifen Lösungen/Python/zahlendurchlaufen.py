# Eingabe der Obergrenze
grenze = int(input("Bis zu welcher Zahl soll gezählt werden? "))

anzahl_gerade = 0
anzahl_ungerade = 0
summe_gerade = 0
summe_ungerade = 0

for i in range(0, grenze + 1):

    if i % 2 == 0:
        print(i, "ist gerade.", end=" ")
        anzahl_gerade += 1
        summe_gerade += i
    else:
        print(i, "ist ungerade.", end=" ")
        anzahl_ungerade += 1
        summe_ungerade += i

    if i % 3 == 0:
        print("(durch 3 teilbar)")
    else:
        print()

print("\nAuswertung:")
print("Anzahl gerader Zahlen:", anzahl_gerade)
print("Anzahl ungerader Zahlen:", anzahl_ungerade)
print("Summe der geraden Zahlen:", summe_gerade)
print("Summe der ungeraden Zahlen:", summe_ungerade)