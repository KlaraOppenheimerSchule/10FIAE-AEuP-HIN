
fixum = float(input("Fixum? "))
umsatz = float(input("Umsatz? "))
gehalt = 0
provision = 0

if umsatz <= 100000:
    provision = 2
else:
    if umsatz <= 500000:
        provision = 3
    else: provision = 5

gehalt = fixum + umsatz*provision/100

print(gehalt)
