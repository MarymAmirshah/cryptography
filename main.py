import random
import numpy as np


def is_prime(x: int):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(np.sqrt(x)), 2):
            if x % i == 0:
                return False

    return True


def share_secret():
    print("----SECRET SHARING----")
    n = 0
    t = 1
    while n < t:
        print("n= ", end="")
        n = int(input())
        print("t= ", end="")
        t = int(input())
        if n <= t:
            print("t should be less or equal than n")
    S = 1
    p = 0
    while p < S:
        print("S= ", end="")
        S = int(input())
        while not is_prime(p):
            print("p= ", end="")
            p = int(input())
            if not is_prime(p):
                print("please enter a prime number for p")
        if S >= p:
            print("please choose a bigger p than S")

    a = np.zeros(t)
    a[0] = S
    for i in range(1, t):
        a[i] = random.randint(-10, 10)

    x = np.zeros(n)
    for i in range(0, n):
        x[i] = i+1

    y = np.zeros(n)
    for i in range(0, n):
        tmp = 0
        for j in range(0, t):
            tmp += a[j] * pow(x[i], j)

        y[i] = tmp.__mod__(p)

    for i in range(0, n):
        print(f'({x[i]}, {y[i]})')


def mod_inverse(a: int, p: int):
    for i in range(1, p):
        x = a*i
        if x.__mod__(p) == 1:
            return i


def get_secret():
    print("----SECRET REVEALING----")
    print("t= ", end="")
    t = int(input())
    p = 0
    while not is_prime(p):
        print("p= ", end="")
        p = int(input())
        if not is_prime(p):
            print("please enter a prime number for p")

    y = np.zeros(t)
    x = np.zeros(t)
    for i in range(0, t):
        print(f'x[{i+1}]= ', end="")
        x[i] = int(input())
        print(f'y[{i+1}]= ', end="")
        y[i] = int(input())

    S = 0
    for i in range(0, t):
        tmp = 1
        for j in range(0, t):
            if i != j:
                tmp1 = x[j] - x[i]
                tmp1 = mod_inverse(tmp1, p)
                tmp2 = x[j] * tmp1
                tmp2 = tmp2.__mod__(p)
                tmp *= tmp2
        S += (y[i]*tmp).__mod__(p)

    print(f'S= {S.__mod__(p)}')


share_secret()
get_secret()
