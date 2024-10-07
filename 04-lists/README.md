# Was sind Listen?

In der Programmierung gibt es eine Datenstruktur, die "Liste" oder "Array" genannt wird.
Eine Liste ist eine Sammlung von Werten, die unter einem Namen gespeichert
sind und innerhalb des Programms verwendet werden können.

Stell dir vor, du möchtest eine Liste von Zahlen erstellen, um später damit zu arbeiten.
Du könntest eine Variable für jede Zahl erstellen, aber das würde sehr unpraktisch werden,
wenn du viele Zahlen hast.

```python
zahl_1 = 1
zahl_2 = 2
zahl_3 = 3

# Alle Inhalte der Liste ausgeben
print("Die Zahlen sind [" + zahl_1 + ", " + zahl_2 + ", " + zahl_3 + "]")

# Die erste Zahl ausgeben
print("Die erste Zahl ist " + zahl_1)
```

Bei dieser Implementation währe es sehr schwierig eine Vierte, Fünfte oder sogar Sechste Zahl hinzuzufügen
und diese herauszugeben.

Stattdessen kannst du eine Liste erstellen,
die alle Zahlen enthält, und diese Liste dann innerhalb deines Programms verwenden.

Eine Liste kann verschiedene Datentypen wie Zahlen, Wörter oder
Booleans enthalten und ist oft eine nützliche Möglichkeit, um eine
Sammlung von Daten zu verwalten. Du kannst beispielsweise eine Liste
von Benutzernamen oder eine Liste von Produktpreisen erstellen.

Insgesamt ist eine Liste oder ein Array eine wichtige Datenstruktur in der Programmierung,
die es uns ermöglicht, eine Sammlung von Daten zu speichern
und zu verwalten, auf die wir später zugreifen können.

## Beispiel in Python

```python
# Eine Liste mit dem Namen "zahlen" wird erstellt und die Zahlen 1, 2 und 3 werden hinzugefügt
zahlen = [1, 2, 3]

# Alle Inhalte der Liste ausgeben
# NOTE: Die str() Funktion wandelt die Liste in einen Text um, welcher von der print() Funktion ausgegeben werden kann
print("Die Zahlen sind " + str(zahlen))

# Die erste Zahl ausgeben
# ???
```

Jetzt ist aber die Frage, wie man die erste Zahl ausgeben kann?

Um auf ein Element der Liste zuzugreifen, muss man den sogenannten "Index" verwenden. Der Index ist die Position des
Elementes in der Liste. Jedoch fängt die Position von Listen in den meisten Programmiersprachen wie Python nicht bei 1,
sondern bei 0 an

```python
# Eine Liste mit dem Namen "zahlen" wird erstellt und die Zahlen 1, 2 und 3 werden hinzugefügt
zahlen = [1, 2, 3]

# ...

# Die erste Zahl ausgeben
# 0 ist hier der Index des ersten Elementes. Um auf ein Element zuzugreifen, muss man immer eckige Klammern [] verwenden.
print(zahlen[0])

# Man kann natürlich auch eine variable verwenden, um auf ein Element zuzugreifen
index_vom_zweiten_element = 1
print(zahlen[index_vom_zweiten_element])
```

Um ein Element zu einer Liste hinzuzufügen, kann man die `append()` Funktion verwenden.

```python
# Eine Liste mit dem Namen "zahlen" wird erstellt und die Zahlen 1, 2 und 3 werden hinzugefügt
zahlen = [1, 2, 3]

# ...

# Alle Inhalte der Liste ausgeben
# NOTE: Die str() Funktion wandelt die Liste in einen Text um, welcher von der print() Funktion ausgegeben werden kann
print("Die Zahlen sind " + str(zahlen)) # -> [1, 2, 3]

# ...

# Die Zahl 4 zur Liste hinzufügen
zahlen.append(4)

print("Die Zahlen sind " + str(zahlen)) # -> [1, 2, 3, 4]
```

## Aufgabe

Erstelle eine Liste mit 5 verschiedenen Wohnorten und gib diese Liste auf der Konsole aus.