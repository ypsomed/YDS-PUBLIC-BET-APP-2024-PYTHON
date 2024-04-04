# Was sind Listen?

In der Programmierung gibt es eine Datenstruktur, die "Liste" oder "Array" genannt wird.
Eine Liste ist eine Sammlung von Werten, die unter einem Namen gespeichert
sind und innerhalb des Programms verwendet werden können.

Stell dir vor, du möchtest eine Liste von Zahlen erstellen, um später damit zu arbeiten.
Du könntest eine Variable für jede Zahl erstellen, aber das würde sehr unpraktisch werden,
wenn du viele Zahlen hast. Stattdessen kannst du eine Liste erstellen,
die alle Zahlen enthält, und diese Liste dann innerhalb deines Programms verwenden.

Eine Liste kann verschiedene Datentypen wie Zahlen, Wörter oder
Booleans enthalten und ist oft eine nützliche Möglichkeit, um eine
Sammlung von Daten zu verwalten. Du kannst beispielsweise eine Liste
von Benutzernamen oder eine Liste von Produktpreisen erstellen.

Um auf ein Element in der Liste zuzugreifen, musst du den Index
des Elements angeben, den du verwenden möchtest. Der Index ist einfach eine Nummer,
die angibt, wo sich das Element in der Liste befindet.
Der erste Index in einer Liste ist immer 0, der zweite Index ist 1 und so weiter.

Insgesamt ist eine Liste oder ein Array eine wichtige Datenstruktur in der Programmierung,
die es uns ermöglicht, eine Sammlung von Daten zu speichern
und zu verwalten, auf die wir später zugreifen können.

## Beispiel in Python

```python
# Eine Liste mit dem Namen "zahlen" wird erstellt und die Zahlen 1, 2 und 3 werden hinzugefügt
zahlen = [1, 2, 3]
# Die Liste "zahlen" wird ausgegeben
print(zahlen)

# Die Variable "zahlen" wird auf den Wert [1, 2, 3, 4] geändert
zahlen = [1, 2, 3, 4]
# Die Liste "zahlen" wird ausgegeben
print(zahlen)

# Die zweite Zahl der Liste wird ausgegeben
print(zahlen[1])

# Man kann auch diese Zahlen zusammenrechnen
print(zahlen[1] + zahlen[0])  # (2 + 1) Da zahlen[1] = 2 und zahlen[0] = 1

# Man kann auch mit variablen auf daten in einer Liste zugreifen
index = 0
print(zahlen[index])  # 1

# Mit len() kann man die länge einer Liste auslesen
# Die Liste "zahlen" hat 4 Element, darum wird die Zahl 4 zurückgegeben
print(len(zahlen))  # 4
```

## Schlaufen

Wenn man irgendeinen Befehl für jedes Element einer Liste ausführen möchte, könnte man es wie gefolgt machen.

```python
# Das Ziel ist es, jede Zahl mit 2 zu addieren und das resultat auf der Konsole auszugeben

# Die Variable "zahlen" wird mit dem Wert [1, 2, 3, 4] erstellt
zahlen = [1, 2, 3, 4]

print(zahlen[0] + 2)  # 3 (1 + 2)
print(zahlen[1] + 2)  # 4 (2 + 2)
print(zahlen[2] + 2)  # 5 (3 + 2)
print(zahlen[3] + 2)  # 6 (4 + 2)
```

Dieser Code funktioniert, jedoch ist er nicht sehr effizient.
Stell dir jetzt vor, dass du eine Liste mit 1000 Elementen hast.
Es wäre doch sehr nervig, wenn man für jede Zahl eine neue Linie Code schreiben müsste.

Hier kommen jetzt Schleifen ins Spiel.
Mit Schleifen kann man ein Stück Code mehrmals ausführen.

```python
zahlen = [1, 2, 3, 4]

# Wir erstellen eine variable, damit wir wissen bei welcher wiederholung wir sind
wiederholung = 0

# Hier wird eine Schleife erstellt, die sich 4 Mal wiederholt
# Auf Deutsch übersetzt würde sich dieser Code grob auf 
# "führe diesen Code aus, während die variable "wiederholung" kleiner als 4 ist" übersetzen
while wiederholung < 4:
    # Hier können wir jetzt einfach mit einer Linie die Zahl mit 2 addieren und sie ausgeben
    # Da die variable "wiederholung" bei jedem durchlauf der schleife um 1 erhöht wird, können wir sehr einfach 
    # auf die Zahl in der Liste zugreifen
    print(zahlen[wiederholung] + 2)

    # Wir müssen die variable "wiederholung" erhöhen, damit diese Schleife nicht unendlich lang läuft
    wiederholung = wiederholung + 1
```

> Meistens wird der variable die in der Schleife erhöht wird, in diesem Fall "wiederholung", den Namen "i"  gegeben
> um Platz zu sparen

Als kleine verbesserung, könnte man
`while wiederholung < 4` mit `while wiederholung < len(zahlen)` ersetzen damit man die Zahl nicht anpassen muss, wenn
man ein neues Element zur Liste hinzufügt.

### Optional: "for" Schleife

```python
zahlen = [1, 2, 3, 4]
# Hier erstellen wir eine Schleife mit Hilfe von "for i in range()", 
# wobei "i" eine variable ist, die sich bei jedem Durchlauf der Schleife ändert.
# Die range-Funktion erzeugt eine Sequenz von Zahlen, beginnend bei 0 und endend bei der angegebenen Zahl (exklusiv).
# In diesem Fall wird "i" nacheinander die Werte 0, 1, 2 und 3 annehmen, 
# da len(zahlen) die Länge der Liste "zahlen" ist, also 4.
for i in range(len(zahlen)):
    # Hier fügen wir 2 zur aktuellen Zahl in der Liste hinzu und geben das Ergebnis aus.
    # Durch "zahlen[i]" greifen wir auf jedes Element der Liste zu, während "i" sich ändert.
    print(zahlen[i] + 2)
```

Diese for i in range() Schleife funktioniert ähnlich wie die while Schleife, jedoch bietet sie eine kompaktere Schreibweise 
und ist oft einfacher zu lesen und zu schreiben. range(len(zahlen)) erzeugt eine Sequenz von Zahlen von 0 bis zur Länge
der Liste zahlen, sodass wir leicht auf jedes Element der Liste zugreifen können. Die Variable i wird bei jedem
Schleifendurchlauf um eins erhöht und ermöglicht uns, nacheinander auf jedes Element der Liste zuzugreifen.

## Aufgabe

Erstelle eine Liste mit Namen von Ortschaften. Erstelle eine Schlaufe, die jeden Ort ausgibt.
Für jeden Ort prüfst du, ob der Ort mit deinem Wohnort übereinstimmt, welchen du ebenfalls in einer Variable speicherst.
Wenn ja, gib "Ich wohne in <Ort>" auf der Konsole aus.
Wenn nicht, gib "Ich wohne nicht in <Ort>" auf der Konsole aus.

Öffne nun die Datei "script.py" und schreibe den Code dort hinein.
