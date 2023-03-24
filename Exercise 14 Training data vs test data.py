import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():
    train_file = StringIO(train_string)
    test_file = StringIO(test_string)

    np.set_printoptions(precision=1) 
    # Please write your code inside this function

    # read in the training data and separate it to x_train and y_train
    data_train = np.genfromtxt(train_file, skip_header=1)
    data_test = np.genfromtxt(test_file, skip_header=1)

    x_train = data_train[:,:-1]


    y_train = data_train[:,-1]

    c = np.asarray([])
    c = np.linalg.listasq(x_train, y_train, rcond=None)[0]

    x_test = data_test[:, :-1]

    print(c.flatten())
    print(x_test @ c)



main()
