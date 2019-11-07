from numpy.random import permutation
from numpy import concatenate
from math import floor


def gen(frac, n):
    p = permutation(n) + 1
    outvec = p
    while p.size > 1:
        p = p[0:floor(frac * p.size)]
        outvec = concatenate([outvec, p])
    return permutation(outvec)


if __name__ == '__main__':
    out = gen(0.3, 70002)
    print(out)
    print('size = {}'.format(out.size))
