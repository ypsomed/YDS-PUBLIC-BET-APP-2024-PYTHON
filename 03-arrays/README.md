# Was sind Konditionen ( if/else )

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

# Durchlaufen einer Liste
for zahl in zahlen:
    print(zahl)
```

## Aufgabe

Erstelle eine Liste mit Namen von Ortschaften. Erstelle eine Schlaufe, die durch die Liste läuft und jeden Ort ausgibt.
Für jeden Ort prüfst du ob der Ort mit deinem Wohnort übereinstimmt, welchen du ebenfalls in einer Variable speicherst.
Wenn ja, gib "Ich wohne in <Ort>" aus.
Wenn nicht, gib "Ich wohne nicht in <Ort>" aus.

Öffne nun die Datei "script.py" und schreibe den Code dort hinein.
