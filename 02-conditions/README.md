# Was sind Konditionen ( if/else )

In der Programmierung gibt es eine Anweisung, die "if/else Statement" genannt wird.
Das ist eine Art von "Entscheidungshilfe", die es dem Programm ermöglicht,
verschiedene Aktionen auszuführen, je nachdem, ob eine bestimmte Bedingung erfüllt ist oder nicht.

Ein Beispiel: Stell dir vor, du hast ein Programm geschrieben,
das den Nutzern eine Nachricht senden soll, wenn sie sich auf einer Website registrieren.
Wenn die Nutzer älter als 13 Jahre alt sind, soll das Programm "Willkommen!" schreiben.
Wenn sie jünger als 13 sind, soll es "Du musst mindestens 13 Jahre alt sein, um dich zu registrieren" schreiben.

Das if/else Statement ermöglicht es, diese Bedingungen zu überprüfen und entsprechend zu handeln.
Wenn die Bedingung erfüllt ist, wird der Code im "if" -Block ausgeführt, sonst wird der Code im "else" -Block ausgeführt.

Insgesamt ist das if/else Statement eine sehr wichtige Anweisung in der Programmierung,
die es uns ermöglicht, Entscheidungen zu treffen und den Programmfluss zu steuern,
basierend auf verschiedenen Bedingungen.

## Beispiel in Python

```python
# Eine Variable mit dem Namen "alter" wird erstellt und der Wert 15 zugewiesen
alter = 15
# Wenn die Bedingung "alter > 13" erfüllt ist, wird der Code im if-Block ausgeführt
if alter > 13:
    print("Willkommen!")
# Wenn die Bedingung "alter > 13" nicht erfüllt ist, wird der Code im else-Block ausgeführt
else:
    print("Du musst mindestens 13 Jahre alt sein, um dich zu registrieren")

# Die Variable "alter" wird auf den Wert 10 geändert
alter = 10
# Wenn die Bedingung "alter > 13" erfüllt ist, wird der Code im if-Block ausgeführt
if alter > 13:
    print("Willkommen!")
# Wenn die Bedingung "alter > 13" nicht erfüllt ist, wird der Code im else-Block ausgeführt
else:
    print("Du musst mindestens 13 Jahre alt sein, um dich zu registrieren")
```

## Aufgabe

Erstelle eine Variable mit dem Namen "wohnort" und speichere deinen Wohnort in der Variable.
Erstelle eine zweite Variable mit "wohnort", wo du den Wert "Berlin" speicherst.
Prüfe, ob der Wert der Variablen "wohnort" gleich dem Wert von einem Wohnort ist.
Wenn ja, gib "Ich wohne in <Wohnort>" aus.
Wenn nicht, gib "Ich wohne nicht in <Wohnort>" aus.

Du kannst prüfen, ob Werte gleich sind indem du den Vergleichsoperator "==" verwendest.
