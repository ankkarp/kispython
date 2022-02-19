import sys
import scipy.constants as sconst


def ex2():
    # print(pow(sys.maxsize, sys.maxsize))
    print(sys.float_info.max)
    print(divmod(38, 5))
    print(len('HmLwvbzBGuahip5ue4oDLw3qLojqWWhDMnbtzLZ0Cw'), 92 % 50, int(420 / 10), int('42'), round(41.6), 21 * 2,
          divmod(92, 50)[1], int(42.9), 40 + 2, (100 - 79) * 2)


def ex3():
    print('standard acceleration of gravity on Earth:', sconst.g, '\nNewtonian constant of gravitation', sconst.G)
    __import__("__hello__")


def ex4(a):
    b = a + a
    c = b + b
    d = c + b
    res = d + d
    print(res)
    b = a + a
    c = b + b
    d = c + c
    res = d + d
    print(res)
    b = a + a
    c = b + b
    d = c + c
    res = d + d - a
    print(res)
    b = a + a
    c = b + a
    d = c + c
    e = d + d
    f = e + e
    res = f + d - a
    print(res)


# ex5: True = 1, False = 0 =>   (True * 2 + False) * -True = (1*2+0)*-1 = -2


if __name__ == '__main__':
    ex = int(input())
    while ex:
        if ex == 2:
            ex2()
        elif ex == 3:
            ex3()
        elif ex == 4:
            ex4(int(input()))
        else:
            break
        ex = int(input())
