# Funktionen

Wenn man ein Stück code wiederverwenden will, damit man ihn nicht Kopieren muss, kann man Funktionen verwenden.
Als Beispiel haben wir hier ein Stück Code, welches mehrere Benutzer begrüsst.

```python
ansprache_mann = "Herr"
ansprache_frau = "Frau"

benutzer_1 = "Tim"
print("Hallo und Willkommen " + ansprache_mann + " " + benutzer_1)
print("Wir hoffen das Sie eine gute Erfahrung haben")

benutzer_2 = "Miloh"
print("Hallo und Willkommen " + ansprache_mann + " " + benutzer_2)
print("Wir hoffen das Sie eine gute Erfahrung haben")

benutzer_3 = "Silas"
print("Hallo und Willkommen " + ansprache_mann + " " + benutzer_3)
print("Wir hoffen das Sie eine gute Erfahrung haben")
```

Hier sieht man aber dass das gleiche Stück Code dreimal wiederholt wurde. Um diesen Code effizienter zu gestalten, kann
man die geteilte Funktionalität in eine neue Funktion auslagern.

Funktionen werden mit dem `def` keyword deklariert. Man muss einer Funktion immer einen Namen geben, mit dem sie später
aufgerufen werden kann. In den Klammern kann eine Funktion mehrere Parameter entgegennehmen, welche beim Aufrufen
mitgegeben werden sollen.

```python
ansprache_mann = "Herr"
ansprache_frau = "Frau"


# Eine Funktion mit dem Namen "begruessen" und den Parametern [name]
def begruessen(ansprache, nachname):
    print("Hallo und Willkommen " + ansprache + " " + nachname)
    print("Wir hoffen das Sie eine gute Erfahrung haben")


benutzer_1 = "Leuenberger"
begruessen(ansprache_mann, benutzer_1)

benutzer_2 = "Zwahlen"
begruessen(ansprache_mann, benutzer_2)

benutzer_3 = "Mächler"
begruessen(ansprache_mann, benutzer_3)
```

Eine Änderung am Begrüssungscode zu machen ist jetzt trivial, da er jetzt nur noch in einer einzigen Funktion vorhanden
ist.

## Rückgabewerte

Funktionen können nicht nur Werte als Parameter entgegennehmen, sondern auch Werte als Rückgabewerte an den aufrufenden
Code zurückgeben.

Als beispiel haben wir hier eine Funktion, welche zu einer beliebigen Zahl 1 addiert

```python
def hinzufuegen(zahl):
    print(zahl + 1)


hinzufuegen(3)  # -> 4
```

Wenn man zum Beispiel die Funktion mit der Zahl "3" aufruft, wird die Zahl "4" ausgegeben.

Was würde man jetzt aber machen, wenn man
die Zahl, welche um 1 erhöht wurde, in einer anderen Funktion mal zwei multiplizieren will? Man muss irgendwie das
Resultat der Funktion an den aufrufenden Code zurückgeben. Dafür kann man einen Rückgabewert verwenden.

Ein rückgabewert wird mithilfe eines `return` Wortes notiert.

```python
def hinzufuegen(zahl):
    # Hier wird die Zahl mithilfe von 'return' zurückgegeben
    return zahl + 1


# Hier ist zahl_plus_eins das Resultat der hinzufuegen Funktion
zahl_plus_eins = hinzufuegen(3)
print(zahl_plus_eins)  # -> 4
```

Jetzt können wir ohne Problem eine zweite Funktion erstellen und die zurückgegebene Zahl als Parameter mitgeben.

```python
def hinzufuegen(zahl):
    # Hier wird die Zahl mithilfe von 'return' zurückgegeben
    return zahl + 1


def mal_zwei(zahl):
    return zahl * 2


zahl_plus_eins = hinzufuegen(3)
print(zahl_plus_eins)  # -> 4

zahl_mal_zwei = mal_zwei(zahl_plus_eins)
print(zahl_mal_zwei)  # -> 8
```

## Aufgabe

Erstelle eine Funktion namens login, welche einen Namen als Parameter nimmt. In der Funktion soll überprüft werden, ob
der
eingegebene Namen mit deinem eigenen Namen übereinstimmt. Falls dies der Fall ist soll der folgende Text ausgegeben
werden

```
Guten Tag <name>
Willkommen bei der Applikation
```

Falls der Name nicht übereinstimmt, soll es in der Konsole `Du kannst dich hier nicht einloggen` anzeigen