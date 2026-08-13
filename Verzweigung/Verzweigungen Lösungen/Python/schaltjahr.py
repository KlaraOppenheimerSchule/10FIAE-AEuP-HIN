jahr = int(input("Geben Sie eine Jahreszahl ein: \n"))
if ((jahr % 400 == 0) or (jahr % 4 == 0 and jahr % 100 != 0)):
     print("Schaltjahr")
else:
     print("kein Schaltjahr")
