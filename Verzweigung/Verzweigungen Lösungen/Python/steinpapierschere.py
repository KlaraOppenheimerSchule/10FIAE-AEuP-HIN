spieler1 = int(input("Spieler 1 (1=Stein, 2=Papier, 3=Schere): "))
spieler2 = int(input("Spieler 2 (1=Stein, 2=Papier, 3=Schere): "))

if spieler1 == spieler2:
    print("Unentschieden")
else:
    if spieler1 == 1:
        if spieler2 == 3:
            print("Spieler 1 gewinnt!")
        else:
            print("Spieler 2 gewinnt!")

    else:
        if spieler1 == 2:
            if spieler2 == 1:
                print("Spieler 1 gewinnt!")
            else:
                print("Spieler 2 gewinnt!")

        else:
            if spieler2 == 2:
                print("Spieler 1 gewinnt!")
            else:
                print("Spieler 2 gewinnt!")