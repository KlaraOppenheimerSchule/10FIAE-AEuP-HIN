# 1. Anlegen
noten = [3, 2, 4, 1, 5]
print('Noten:', noten)

# 2. Note hinzufügen
noten.append(4)

# 3. Durschnittsnote
len = 0
sum = 0
for note in noten:
    len +=1
    sum = sum + note
    
avg = sum/len
print('Durchschnitt:', round(avg,2))
