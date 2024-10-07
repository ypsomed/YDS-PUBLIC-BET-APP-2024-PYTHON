mein_name = "Tim"

# Hier wird eine Funktion erstellt, welche ein User begrüsst, wenn er eingeloggt wird
def login(name):
    if name == mein_name:
        print("Guten Tag " + name)
        print("Willkommen bei der Applikation")
    else:
        print("Du kannst dich hier nicht einloggen")


# Wird eingeloggt
login("Tim")

# Wird nicht eingeloggt
login("Silas")


