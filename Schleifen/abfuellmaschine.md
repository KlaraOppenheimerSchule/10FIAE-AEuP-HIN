# Abfüllmaschine


### Schwierigkeitsgrad: ***


Eine Getränkeabfüllmaschine soll Flaschen mit genau 500 ml befüllen. Leider ist die Maschine fehlerhaft und füllt manchmal zu wenig oder zu viel ein. Sie sollen ein Programm schreiben, das die Maschine testet.


Situation:  
•	Es werden 10 Flaschen nacheinander befüllt.  
•	Für jede Flasche wird die tatsächlich eingefüllte Menge (in ml) vom Benut-zer eingegeben.  
•	Wenn die Menge zwischen 490 und 510 ml liegt, gilt die Flasche als akzep-tabel.  
•	Ist die Menge außerhalb dieses Bereichs, wird die Flasche aussortiert.  
•	Nach jeder Flasche soll der Benutzer gefragt werden, ob er den Test fortset-zen möchte (j für ja, n für nein). Wenn n eingegeben wird, wird der Test vor-zeitig abgebrochen.


**Beispielausgabe**  
Flasche 1: Wie viel ml wurden eingefüllt? 495  
→ akzeptabel  
Weiter testen? (j/n): j 


Flasche 2: Wie viel ml wurden eingefüllt? 520  
→ aussortiert  
Weiter testen? (j/n): j  
...


Test beendet.  
Akzeptable Flaschen: 6  
Aussortierte Flaschen: 3


