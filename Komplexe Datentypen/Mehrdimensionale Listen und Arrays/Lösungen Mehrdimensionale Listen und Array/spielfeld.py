#1 

brett = [[' ']*3 for _ in range(3)]
for zeile in brett:
    print('|'.join(zeile))

#2
z = int(input("Zeile?: "))
s = int(input("Spalte?: "))

if brett[z][s] == ' ':
        brett[z][s] = "X"
        print(True)   
else:
    print(False)

for zeile in brett:
    print('|'.join(zeile))
