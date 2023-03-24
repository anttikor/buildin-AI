import random

def main():
    favourite = " nothing"
    rand = 0.00
    while rand == 0.00:
        rand = random.random()

    if rand > 0.80:
        favourite = "bats"
        if rand > 0.90:
            favourite = "cats"
    else:
        favourite = "dogs"
    print (rand)
    print("I love " + favourite) 


main()