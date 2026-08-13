pin = int(input("PIN eingeben: "))

if pin == 1234:

    kontostand = float(input("Kontostand in Euro: "))
    betrag = float(input("Auszahlungsbetrag in Euro: "))

    if betrag <= 500:

        if betrag % 10 == 0:

            if betrag > 300:
                gebuehr = 5
            else:
                gebuehr = 0

            if kontostand >= betrag + gebuehr:

                neuer_kontostand = kontostand - betrag - gebuehr

                if neuer_kontostand >= 50:

                    print("PIN korrekt.")
                    print("Gebühr:", gebuehr, "Euro")
                    print("Auszahlung erfolgreich.")
                    print("Neuer Kontostand:", neuer_kontostand, "Euro")

                else:
                    print("Nach der Auszahlung müssen mindestens 50 Euro auf dem Konto bleiben.")

            else:
                print("Nicht genügend Guthaben vorhanden.")

        else:
            print("Der Betrag muss durch 10 teilbar sein.")

    else:
        print("Maximal 500 Euro pro Auszahlung erlaubt.")

else:
    print("PIN falsch. Zugriff verweigert.")