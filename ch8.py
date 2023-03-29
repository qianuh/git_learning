# ensure the input is int

while True:
    try:
        a = int(input("input an int : "))
    except ValueError:
        print("You dont input an int .  Try again...")

