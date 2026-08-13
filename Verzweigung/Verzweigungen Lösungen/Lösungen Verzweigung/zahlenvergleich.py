zahl1 = int(input("Erste Zahl eingeben: "))
zahl2 = int(input("Zweite Zahl eingeben: "))

if zahl1 > zahl2:
    print("Die erste Zahl ist größer.")
else:
    if zahl2 > zahl1:
        print("Die zweite Zahl ist größer.")
    else:
        print("Beide Zahlen sind gleich.")