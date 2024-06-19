from random import *
from turtle import *

start_x = -400
ziel_x = 500

turtle_1_fortschritt = 0
turtle_2_fortschritt = 0
turtle_3_fortschritt = 0
turtle_4_fortschritt = 0

# Alle Turtles erstellen
turtle_1 = Turtle()
turtle_1.penup()
turtle_1.goto(start_x, -20)
turtle_1.shape("turtle")

turtle_2 = Turtle()
turtle_2.penup()
turtle_2.goto(start_x, 0)
turtle_2.shape("turtle")

turtle_3 = Turtle()
turtle_3.penup()
turtle_3.goto(start_x, 20)
turtle_3.shape("turtle")

turtle_4 = Turtle()
turtle_4.penup()
turtle_4.goto(start_x, 40)
turtle_4.shape("turtle")

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
    turtle_1_hinzufuegen = randrange(0, 5)
    turtle_2_hinzufuegen = randrange(0, 5)
    turtle_3_hinzufuegen = randrange(0, 5)
    turtle_4_hinzufuegen = randrange(0, 5)

    turtle_1_fortschritt += turtle_1_hinzufuegen
    turtle_2_fortschritt += turtle_2_hinzufuegen
    turtle_3_fortschritt += turtle_3_hinzufuegen
    turtle_4_fortschritt += turtle_4_hinzufuegen

    turtle_1.forward(turtle_1_hinzufuegen)
    turtle_2.forward(turtle_2_hinzufuegen)
    turtle_3.forward(turtle_3_hinzufuegen)
    turtle_4.forward(turtle_4_hinzufuegen)

    # Wenn einer der fortschritte der Turtles grösser ist als `ziel_x`, soll das Rennen beendet werden
    if turtle_1_fortschritt >= ziel_x:
        print("Turtle 1 hat gewonnen!")
        turtle_1.color("red")
        break

    if turtle_2_fortschritt >= ziel_x:
        print("Turtle 2 hat gewonnen!")
        turtle_2.color("red")
        break

    if turtle_3_fortschritt >= ziel_x:
        print("Turtle 3 hat gewonnen!")
        turtle_3.color("red")
        break

    if turtle_4_fortschritt >= ziel_x:
        print("Turtle 4 hat gewonnen!")
        turtle_4.color("red")
        break

done()
