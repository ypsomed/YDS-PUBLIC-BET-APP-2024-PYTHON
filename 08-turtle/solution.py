from turtle import *

# Zeichnen eines Quadrats
goto(0, 0)
pendown()

for _ in range(4):
    forward(100)
    left(90)

penup()

clear()

# Zeichnen eines Dreiecks
goto(0, 0)
pendown()

for _ in range(3):
    forward(100)
    left(120)

penup()

clear()

# Zeichnen eines Sterns
goto(0, 0)
pendown()

for _ in range(5):
    forward(100)
    left(144)

penup()

clear()

# Zeichnen eines Kreises
goto(0, 0)
pendown()

radius = 1
for _ in range(360):
    forward(radius)
    right(1)

penup()
clear()

# Zeichnen eines Baumes
goto(0, 0)
pendown()


def zeichne_ast(ast_laenge):
    if ast_laenge < 5:
        # Brich die Funktion ab
        return

    forward(ast_laenge)
    right(25)
    zeichne_ast(ast_laenge - 15)
    left(50)
    zeichne_ast(ast_laenge - 15)
    right(25)
    backward(ast_laenge)


left(90)
zeichne_ast(80)

penup()

done()
