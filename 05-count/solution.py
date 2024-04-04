zahl = input("Gib eine Zahl ein: ")

if not zahl.isdigit():
    print("Das ist keine ganze Zahl!")
else:
    zahl = int(zahl)
    for i in range(1, zahl + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
