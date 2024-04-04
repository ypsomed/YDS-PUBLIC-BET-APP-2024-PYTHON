# Definiere eine Liste von Zahlen
zahlen = [2, 4, 6, 8, 10]

# Initialisiere die Summe
summe = 0

# Schleife durch die Liste und berechne die Summe
for zahl in zahlen:
    summe += zahl

# Berechne den Durchschnitt
durchschnitt = summe / len(zahlen)

# Prüfe, ob der Durchschnitt größer als 10 ist
if durchschnitt > 10:
    print("Der Durchschnitt ist größer als 10")
else:
    print("Der Durchschnitt ist kleiner als 10")
