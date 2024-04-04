import random

# Wörterliste
words = ["python", "programmierung", "computer", "daten", "variable", "funktion"]

# Zufälliges Wort auswählen
word = random.choice(words)

# Anzahl der Versuche
guesses = 10

# Anfangszustand anzeigen
print("Das Wort hat", len(word), "Buchstaben:")
display = "_" * len(word)
print(display)

# Schleife für die Eingabe des Spielers
while guesses > 0 and "_" in display:
    guess = input("Gib einen Buchstaben ein: ").lower()

    if guess in word:
        print("Richtig!")
        # Das Wort aktualisieren, um den geratenen Buchstaben zu zeigen
        for i in range(len(word)):
            if word[i] == guess:
                display = display[:i] + guess + display[i + 1 :]
    else:
        guesses -= 1
        print("Falsch! Du hast noch", guesses, "Versuche übrig.")

    print(display)

# Spiel beenden
if "_" not in display:
    print("Gewonnen! Das Wort war", word)
else:
    print("Verloren! Das Wort war", word)
