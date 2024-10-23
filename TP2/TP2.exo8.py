while True:
    x = float(input("Entrez un nombre décimal : "))
    if (x >= 2 and x < 3) or (x > 0 and x <= 1) or (x >= -10 and x <= -2):
        print("x est dans I ")
    else:
        print("x est hors de I ")