# Getränkeabfüllmaschine-Testprogramm

akzeptabel = 0
aussortiert = 0
flasche = 1

while flasche <= 10:
    print(f"\nFlasche {flasche}:")
    
    # Eingabevalidierungsschleife
    while True:
        
        menge = float(input("Wie viel ml wurden eingefüllt? "))
        if menge <= 0:
            print("Bitte eine positive Zahl eingeben.")
        else:
            break
       
    # Verzweigung zur Bewertung
    if 490 <= menge <= 510:
        print("→ akzeptabel")
        akzeptabel += 1
    else:
        print("→ aussortiert")
        aussortiert += 1

    # Fortsetzungsabfrage
    weiter = input("Weiter testen? (j/n): ").lower()
    if weiter == "n":
        break

    flasche += 1

# Ergebnis
print("\nTest beendet.")
print("Akzeptable Flaschen:", akzeptabel)
print("Aussortierte Flaschen:", aussortiert)
