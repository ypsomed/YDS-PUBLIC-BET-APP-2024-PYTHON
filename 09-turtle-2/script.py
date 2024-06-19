from random import *
from turtle import *

start_x = -400
ziel_x = 500

# Diese Variable ist hier um den fortschritt des ersten Turtles zu behalten und damit zu bestimmen, wann er die ziel
# linie überschritten hat
turtle_1_fortschritt = 0

# TODO: Erstelle drei weiter `turtle_fortschritt` variablen

# Hier wird der erste Turtle erstellt, es sollten noch drei andere Turtles erstellt werden
turtle_1 = Turtle()
turtle_1.penup()
turtle_1.goto(start_x, -20)
turtle_1.shape("turtle")

# TODO: Erstelle drei weitere Turtles

# Zeichne das Ziel
linien_zeichner = Turtle()
linien_zeichner.penup()
linien_zeichner.goto(0, 0)

linien_zeichner.goto(ziel_x + start_x, screensize()[1])
linien_zeichner.pendown()
linien_zeichner.goto(ziel_x + start_x, -screensize()[1])
linien_zeichner.hideturtle()

# Rennen beginnen
# dieser Loop läuft bis im loop der `break` Befehl ausgeführt wird
while True:
    # Mit dem `random` modul kann man zufällige zahlen generieren

    # `randrange()` Generiert eine Zahl von der ersten Zahl bis zur zweiten Zahl
    # Bei `randrange(0, 5)` Währen also die möglichen zahlen: 0, 1, 2, 3, 4
    # Der Turtle soll hier 0 bis 4 Pixel nach vorne fahren
    # TODO: Implementiere dies für die anderen Turtles
    turtle_1_hinzufuegen = randrange(0, 5)

    # Hier wird die gewählte Zahl zum fortschritt hinzugefügt
    # TODO: Implementiere dies für die anderen Turtles
    turtle_1_fortschritt += turtle_1_hinzufuegen

    # Jetzt wird der Turtle die gewählte zahl nach vorne gestossen
    # TODO: Implementiere dies für die anderen Turtles
    turtle_1.forward(turtle_1_hinzufuegen)

    # Wenn einer der fortschritte der Turtles grösser ist als `ziel_x`, soll das Rennen beendet werden.
    # Es soll zusätzlich in der Konsole ausgegeben werden, welcher Turtle gewonnen hat.
    # Der Turtle, der das Spiel gewonnen hat soll rot markiert werden
    # der Loop soll mit dem `break` Befehl gestoppt werden
    # TODO: Implementieren

done()
