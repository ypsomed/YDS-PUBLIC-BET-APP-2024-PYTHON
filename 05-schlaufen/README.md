# Schlaufen

Wenn man ein Programm schreiben will, welches von 1 bis 5 Zählt, könnte man es wie gefolgt implementieren.

```python
# Von 1 bis 5 Zählen
print("1")
print("2")
print("3")
print("4")
print("5")
```

Was wäre, wenn man jetzt aber auf 100 Zählen möchte?
Diesen Code weiterzuführen währe eine Grosse Aufgabe, welche viel Zeit verschwenden würde.

Um diesen Code zu verschönern, währe es vorteilhaft, wenn wir den gleichen Code wiederholen könnten. Hier kommen jetzt
Schlaufen ins Spiel. Mit Schlaufen kann man ein Stück Code wiederholen, bis eine Kondition nicht mehr stimmt.

Die Implementation unseres Beispieles würde mit Schlaufen so aussehen.

```python
# Wie viele Male hat sich der Code schon wiederholt?
wiederholung = 0

# Während die Zahl der Wiederholungen kleiner als fünf ist, wollen wir diesen Code ausführen.
while wiederholung < 100:
    # Da wir schon eine Zahl haben, welche immer erhöht wird, können wir diese hier ausgeben
    print(wiederholung)

    # Damit diese Schlaufe nicht unendlich Lang läuft, müssen wir die wiederholung variable um 1 erhöhen.
    wiederholung = wiederholung + 1
```

> Meistens wird der Variable, die in der Schleife erhöht wird, in diesem Fall "wiederholung", den Namen "i" gegeben
> um Platz zu sparen

## Schlaufen mit Listen

Wir können eine Liste mit einer Schlaufe kombinieren, um alle Elemente einer Liste einzel auszugeben.

```python
wohnorte = [
    "Bern",
    "Zürich",
    "Basel",
    "Luzern",
    "Aarberg"
]

wiederholung = 0

while wiederholung < 5:
    # Wir können hier auf einzelne Elemente zugreifen, wie es im Kapitel 04-lists beschrieben wurde.
    print(wohnorte[wiederholung])
```

Wenn wir jetzt die Grösse der Liste ändern, werden nicht mehr alle Elemente ausgegeben, da der Code nur 5 Mal wiederholt
wird.

```python
wohnorte = [
    "Bern",
    "Zürich",
    "Basel",
    "Luzern",
    "Aarberg",
    "Solothurn"
]

wiederholung = 0

while wiederholung < 5:
    # Wir können hier auf einzelne Elemente zugreifen, wie es im Kapitel 04-lists beschrieben wurde.
    # "Solothurn" wird nicht ausgegeben
    print(wohnorte[wiederholung])

    wiederholung = wiederholung + 1
```

Um sicherzustellen, dass alle Elemente einer Liste ausgegeben werden, müssen wir hier die Zahl der wiederholungen
abändern, damit sie dynamisch mit der Grösse der Liste übereinstimmt.

Dies kann man mithilfe der `len()` Funktion erreichen. Diese Funktion gibt die Grösse einer Liste zurück

```python
wohnorte = [
    "Bern",
    "Zürich",
    "Basel",
    "Luzern",
    "Aarberg",
    "Solothurn"
]

# Hier wird 6 ausgegeben
print(len(wohnorte))
```

Jetzt muss man nur noch die Kondition der Schleife anpassen, damit sie richtig viel Mal wiederholt wird.

```python
...

grösse_wohnorte_liste = len(wohnorte)
while wiederholung < grösse_wohnorte_liste:
    # Wir können hier auf einzelne Elemente zugreifen, wie es im Kapitel 04-lists beschrieben wurde.
    print(wohnorte[wiederholung])

    wiederholung = wiederholung + 1
    
...
```

## Aufgabe

Erstelle eine Liste mit Namen von Ortschaften. Erstelle eine Schlaufe, die jeden Ort ausgibt.
Für jeden Ort prüfst du, ob der Ort mit deinem Wohnort übereinstimmt, welchen du ebenfalls in einer Variable speicherst.
Wenn ja, gib "Ich wohne in <Ort>" auf der Konsole aus.
Wenn nicht, gib "Ich wohne nicht in <Ort>" auf der Konsole aus.

Öffne nun die Datei "script.py" und schreibe den Code dort hinein.
