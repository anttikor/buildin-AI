import numpy as np

def generate(p1):
    seq = (np.random.choice([0,1], p=[1-p1, p1], size=10000))
    return seq #palauttaa listan mihin arvottu 1 ja 0

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    counter_amount = 0 #muuttuja mikä laskee kuinka monta peräkkäistä 5-sarjaa löytyy


    for x in range(0,len(seq)-4):
        if seq[x:x+5].all():
            counter_amount += 1
    return (counter_amount)

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))

