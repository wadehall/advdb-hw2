from numpy.random import permutation
from numpy import concatenate
from math import floor
from random import randrange
from tqdm import tqdm
import os

COLUMN_NAMES = ['stocksymbol', 'time', 'quantity', 'price']

FILE_PATH = 'trade_uniform.csv'
NUM_RECORDS = 10000000
# NUM_STOCKSYMBOLS = 100000
X = 70002

# test
# FILE_PATH = 'trade_uniform_test.csv'
# NUM_RECORDS = 10000
# NUM_STOCKSYMBOLS = 1000
# X = 703


def gen_uniform(n):
    p = permutation(n) + 1
    # outvec = p
    # while p.size > 1:
    #     p = p[0:floor(frac * p.size)]
    #     outvec = concatenate([outvec, p])
    # return permutation(outvec)
    return p


if __name__ == '__main__':
    stocksymbol_sample = gen_uniform(X)

    print('NUM_RECORDS = {}'.format(NUM_RECORDS))
    print('NUM_STOCKSYMBOLS = {}'.format(stocksymbol_sample.size))

    # output
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
    f = open(FILE_PATH, 'w')
    # column names
    f.write(','.join(COLUMN_NAMES) + '\n')
    # data
    prev_price_list = [-1 for i in range(X)]
    for i in tqdm(range(NUM_RECORDS)):
        stocksymbol = stocksymbol_sample[randrange(0, X)]
        time = i
        quantity = randrange(100, 10001)
        price = randrange(50, 501)
        if prev_price_list[stocksymbol - 1] != -1:
            prev_price = prev_price_list[stocksymbol - 1]
            while not (prev_price - 5 <= price <= prev_price - 1 or
                       prev_price + 1 <= price <= prev_price + 5):
                price = randrange(50, 501)
        prev_price_list[stocksymbol - 1] = price

        f.write(
            str(stocksymbol) + ',' +
            str(time) + ',' +
            str(quantity) + ',' +
            str(price) + '\n'
        )
    f.close()
