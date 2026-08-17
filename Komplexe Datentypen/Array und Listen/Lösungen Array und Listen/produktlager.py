
#1. Anlegen und ausgeben
produkte = ['Maus','Tastatur','Monitor','USB-Kabel','Headset']
print('Enthält Monitor?', 'Monitor' in produkte)


#2. Hinzufügen und entfernen
produkte.append('Webcam')
produkte.remove('USB-Kabel')

# 3. Zählen
print('Anzahl:', len(produkte))
