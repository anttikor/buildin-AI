import numpy as np

p1 = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]  # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]  # loaded


def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1
    #for roll in sequence:
        #print("rolled %d" % roll)

    return sequence


def bayes(sequence):
    odds = 1.0  # start with odds 1:1
    #P(conferences ∣ spam)÷P(conferences ∣ ham)=0.0000100÷0.0000391=0.2554
    #P(million ∣ spam)÷P(million ∣ ham)=0.0016285÷0.0003198=5.0923

    #Thus with the first, normal die the probabilities of each side
    # are the same, 0.167 (or 16.7 %). With the second, loaded die,
    #the probability of 6 is 0.5 (or 50 %) and each of the other
    # five sides has probability 0.1 (or 10 %).
    #i = 0
    j = 0
    for roll in sequence:
        #i +=1
        #print(" %i nopan heiton tulos: %i" % (i, roll))
        if roll == 6:
            r = 0.5 / (1/6)
        else:
            r = 0.1 / (1 / 6)
        odds = odds * r
        #print (odds)
    #print("6 tuli %i kertaa" % (j))
    if odds > 1:
        return True
    else:
        return False


sequence = roll(False)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
