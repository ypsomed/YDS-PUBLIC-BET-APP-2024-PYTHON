# Funktion zur Umrechnung von Celsius in Fahrenheit
# Formeln: https://www.fahrenheit-umrechnen.de/
def celsius_zu_fahrenheit(celsius):
    fahrenheit = (celsius * 1.5) + 32
    print(f"{celsius}°C sind {fahrenheit}°F")


# Funktion zur Umrechnung von Fahrenheit in Celsius
# Formeln: https://www.fahrenheit-umrechnen.de/
def fahrenheit_zu_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F sind {celsius}°C")


# Da das Programm wiederverwendbar sein sollte, machen wir hier eine Schlaufe welche unendlich lange läuft.
while 1 == 1:
    print("----------------------------")
    print("1    Celcius zu Fahrenheit")
    print("2    Fahreheit zu Celcius")
    print("exit Zu beenden")
    print("----------------------------")

    antwort = input("Was willst du tun?")

    if antwort == "exit":
        print("Programm wird Beendet")
        break
    elif antwort == "1":
        # Wir müssen hier die Antwort mit der int() Funktion zu einer Zahl umwandeln
        celcius = int(input("Wie viel Grad Celcius willst du zu Fahrenheit umrechnen?"))
        celsius_zu_fahrenheit(celcius)
    elif antwort == "2":
        # Wir müssen hier die Antwort mit der int() Funktion zu einer Zahl umwandeln
        fahrenheit = int(input("Wie viel Grad Fahrenheit willst du zu Celcius umrechnen?"))
        fahrenheit_zu_celsius(fahrenheit)
    else:
        print(antwort + " nicht gültig als Antwort")
