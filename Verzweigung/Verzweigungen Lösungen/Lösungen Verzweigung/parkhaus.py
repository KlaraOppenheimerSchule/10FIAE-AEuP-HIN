anzahl_parkplätze_belegt = int(input("Wie viele Parkplätze sind belegt?"))
eingang_ausgang_block = int(input("Ist der Eingang blockiert? 0 = Nein, 1 = Ja"))
vermietet = int(input("Ist angemietet? 0 = Nein, 1 = Ja"))

if anzahl_parkplätze_belegt > (500*0.95):
    if eingang_ausgang_block == 0:
        print("Parkhaus belegt")
    else:
        print("Parkhaus gesperrt")
else:
    if eingang_ausgang_block == 1 and vermietet==0 or vermietet==1:
        print("Parkhaus gesperrt")
    elif eingang_ausgang_block == 0 and vermietet == 1:
        print("Parkhaus gesperrt")
    else:
        print("Parkhaus frei")

