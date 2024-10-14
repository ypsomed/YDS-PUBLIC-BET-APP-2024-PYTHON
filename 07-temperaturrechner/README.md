# Temperaturrechner

Programmiere eine Applikation, welche eine vom Benutzer eingegebene Zahle von Grad Celsius zu Grad Fahrenheit und
umgekehrt umwandeln kann. Die Applikation soll nach dem Umwandeln weiter verwendbar sein und soll einen Verlauf der
Umwandlungen anzeigen können.

Erstelle je zwei Umwandlungsfunktionen, welche eine Zahl als Parameter nehmen und dieser zu Grad oder Celsius umwandeln
und dann als Rückgabewert zurückgeben. Dieser Rückgabewert soll anschliessen in der Konsole ausgegeben werden. Die
Formel für die Umwandlung von Fahrenheit zu Celsius und Celsius zu Fahrenheit ist
die folgende.

- °C = (°F - 32) * 5/9 (von Fahrenheit in Celsius)
- °F = °C * 1,8 + 32 (von Celsius nach Fahrenheit)

Die Applikation soll dieses Menu anzeigen, um am User mitzuteilen, was er machen kann.

```
----------------------------
1    Celcius zu Fahrenheit
2    Fahreheit zu Celcius
3    Verlauf anzeigen
exit Zu beenden
----------------------------
```

Die Applikation hat die folgenden Befehle

- **1**: Von Celsius zu Fahrenheit umwandeln
- **2**: Von Fahrenheit zu Celsius umwandeln
- **3**: Verlauf anzeigen
- **exit**: Applikation beenden

Der Verlauf der Umwandlungen soll in diesem Format sein

Celsius zu Fahrenheit

> {Index der Umwandlung}. {Grad Celsius}°C -> {Grad Fahrenheit}°F

Fahrenheit zu Celsius

> {Index der Umwandlung}. {Grad Fahrenheit}°F -> {Grad Celsius}°C

Beispiel:

- 0\. 20°C -> 62.0°F
- 1\. 123°F -> 50.55555555555556°C

Für die Applikation werden die folgenden Funktionen verwendet

- `input()`: Eine Eingabe vom User verlangen, als erster Parameter kann man einen Text in der
  Konsole angeben. Der Rückgabewert der Funktion ist die Eingabe des Users
- `int()`: Einen String wie "1" in eine Zahl umwandeln. Diese werden verwendet, da die `input()` Funktion einen String
  zurückgibt
- `break`: Mit dem `break` Befehl kann man eine Schlaufe abbrechen, auch wenn die Kondition immer noch stimmt.
- `return` Mit dem `return` Befehl wird ein Wert von einer Funktion zurückgegeben
- `append()`: Mit dieser Funktion wird die Umwandlung in einer Liste gespeichert.

