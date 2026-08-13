# Äu0ere Schleife ist Teil der Zusatzaufgabe
weitermachen = "j"

while weitermachen == "j":

# Ab hier Hauptaufgabe 
    anschaffungspreis = float(input("Anschaffungspreis in €: "))
    nutzungsdauer = int(input("Nutzungsdauer in Jahren: "))
    grenzwert = float(input("Grenzwert für den Buchwert in €: "))

    jahresabschreibung = anschaffungspreis / nutzungsdauer
    buchwert = anschaffungspreis

    print("\nJahr\tAbschreibung\tBuchwert")

    for jahr in range(1, nutzungsdauer + 1):
        buchwert = buchwert - jahresabschreibung

        print(
            jahr,
            "\t",
            round(jahresabschreibung, 2),
            "€\t\t",
            round(buchwert, 2),
            "€"
        )

        if buchwert < grenzwert:
            print(">>> Achtung: Der Buchwert liegt unter dem Grenzwert!")

    print("\nZusammenfassung")
    print("Anschaffungspreis:", round(anschaffungspreis, 2), "€")
    print("Nutzungsdauer:", nutzungsdauer, "Jahre")
    print("Gesamte Abschreibung:", round(jahresabschreibung * nutzungsdauer, 2), "€")
    print("Restwert:", round(buchwert, 2), "€")

    # Teil der Zusatzaufgabe
    weitermachen = input(
        "\nMöchten Sie ein weiteres Wirtschaftsgut berechnen? (j/n): "
    )