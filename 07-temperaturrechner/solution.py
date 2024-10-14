# Funktion zur Umrechnung von Celsius in Fahrenheit
# Formeln: https://www.fahrenheit-umrechnen.de/
def celsius_zu_fahrenheit(celsius):
    fahrenheit = (celsius * 1.5) + 32
    return fahrenheit


# Funktion zur Umrechnung von Fahrenheit in Celsius
# Formeln: https://www.fahrenheit-umrechnen.de/
def fahrenheit_zu_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# In dieser Liste hier speichern wir den Verlauf der Konvertierungen
verlauf = []

# Da das Programm wiederverwendbar sein sollte, machen wir hier eine Schlaufe welche unendlich lange läuft.
while 1 == 1:
    print("----------------------------")
    print("1    Celcius zu Fahrenheit")
    print("2    Fahreheit zu Celcius")
    print("3    Verlauf Anzeigen")
    print("exit Zu beenden")
    print("----------------------------")

    antwort = input("Was willst du tun?")

    if antwort == "exit":
        print("Programm wird Beendet")
        break
    elif antwort == "1":
        # Wir müssen hier die Antwort mit der int() Funktion zu einer Zahl umwandeln
        celsius = int(input("Wie viel Grad Celcius willst du zu Fahrenheit umrechnen?"))
        fahrenheit = celsius_zu_fahrenheit(celsius)

        # Hier speichern wir den Verlauf
        verlauf.append(str(celsius) + "°C -> " + str(fahrenheit) + "°F")

        print(f"{celsius}°C sind {fahrenheit}°F")
    elif antwort == "2":
        # Wir müssen hier die Antwort mit der int() Funktion zu einer Zahl umwandeln
        fahrenheit = int(input("Wie viel Grad Fahrenheit willst du zu Celcius umrechnen?"))
        celsius = fahrenheit_zu_celsius(fahrenheit)

        # Hier speichern wir den Verlauf
        verlauf.append(str(fahrenheit) + "°F -> " + str(celsius) + "°C")

        print(f"{fahrenheit}°F sind {celsius}°C")
    elif antwort == "3":
        wiederholungen = 0

        while wiederholungen < len(verlauf):
            print(str(wiederholungen) + ". " + verlauf[wiederholungen])
            wiederholungen = wiederholungen + 1
    else:
        print(antwort + " nicht gültig als Antwort")
