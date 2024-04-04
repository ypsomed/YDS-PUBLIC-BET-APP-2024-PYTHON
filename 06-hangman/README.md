# Hangman Spiel

Schreibe ein Python-Skript, das das klassische Spiel "Hangman" implementiert.
Der Computer wählt ein zufälliges Wort aus einer Liste von Wörtern und der
Spieler muss das Wort durch das Erraten von Buchstaben in einer begrenzten Anzahl von Versuchen erraten.

Hier sind die Schritte, die du implementieren musst:

1. Wähle ein zufälliges Wort aus einer Liste von Wörtern.
1. Zeige dem Spieler die Anzahl der Buchstaben im Wort als Unterstriche an (einer für jeden Buchstaben).
1. Der Spieler gibt einen Buchstaben ein.
1. Überprüfe, ob der Buchstabe im Wort vorkommt. Wenn ja, ersetze den entsprechenden Unterstrich durch den Buchstaben.
1. Wenn der Buchstabe nicht im Wort vorkommt, ziehe einen Versuch ab.
1. Wiederhole Schritte 3-5, bis das Wort vollständig geraten ist oder die Anzahl der Versuche aufgebraucht ist.
1. Wenn der Spieler das Wort vollständig erraten hat, gib eine Nachricht aus, die den Spieler beglückwünscht. Wenn der Spieler das Wort nicht erraten hat, gib eine Nachricht aus, die das Wort zeigt.

## Tipps

- Verwende `random.choice()` aus der `random` Bibliothek, um ein zufälliges Wort aus einer Liste auszuwählen.
- Erstelle eine Zeichenfolge mit Unterstrichen (\_) derselben Länge wie das zu erratende Wort.
- Verwende eine `while` Schleife und eine Zählervariable, um die Anzahl der Versuche zu verfolgen.
- Verwende `input()` und `lower()` Methoden, um den vom Benutzer eingegebenen Buchstaben in Kleinbuchstaben umzuwandeln.
- Verwende `in` Operator, um zu überprüfen, ob der eingegebene Buchstabe im Wort vorkommt. Verwende `str.replace()` Methode, um das Wort zu aktualisieren.
- Verwende break Statement, um die Schleife zu beenden, wenn das Wort vollständig erraten wurde oder die Anzahl der Versuche aufgebraucht ist.
- Verwende `print()` Funktion, um eine Nachricht auszugeben, wenn das Wort vollständig erraten wurde oder nicht.
- Verwende `isalpha()` Methode, um zu überprüfen, ob der vom Benutzer eingegebene Wert ein Buchstabe ist.
