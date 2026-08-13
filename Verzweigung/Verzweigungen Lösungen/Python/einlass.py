alter = int(input("Wie alt bist du?"))
begleitung = int(input("Bist du in Begleitung? (0) = Nein, (1) = Ja "))
begleitung_volljaehrig = int(input("Ist mind. eine Begleitung volljähirg? (0) = Nein, (1) = Ja "))

if alter < 18:
    if begleitung == 1:
        if begleitung_volljaehrig == 1:
            print("Willkommen!")
        else:
            print("Du musst leider gehen!")
    else:
        print("Du musst leider gehen!")
else: 
    print("Willkommen!")
