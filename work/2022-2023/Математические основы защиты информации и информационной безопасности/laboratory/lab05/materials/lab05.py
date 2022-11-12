from random import randint
import math


def fermat(n: int) -> bool:
    a = randint(2, n-2)
    r = (a**(n-1)) % n
    return r == 1


def jacobi(a: int, b: int):
    def even(x): return x % 2 == 0
    if math.gcd(a, b) != 1:
        return 0

    r = 1
    if a < 0:
        a = -a
        if b % 4 == 3:
            r = -r

    while True:
        t = 0
        while even(a):
            t += 1
            a //= 2

        if not even(t):
            if b % 8 in (3, 5):
                r = -r

        if a % 4 == b % 4 == 3:
            r = -r

        c = a
        a = b % c
        b = c

        if a == 0:
            return r


def solovay_strassen(n: int) -> bool:
    a = randint(2, n-1)
    if math.gcd(a, n) > 1:
        return False
    if (a**((n-1)//2) - jacobi(a, n)) % n != 0:
        return False
    return True


def miller_rabin(n: int) -> bool:
    def even(x): return x % 2 == 0
    r = n-1
    s = 0
    while even(r):
        s += 1
        r //= 2

    a = randint(2, n-3)

    y = a**r % n
    if y != 1 and y != n-1:
        j = 1
        while j <= s-1 and y != n-1:
            y = y**2 % n
            if y == 1:
                return False
            j += 1
        if y != n-1:
            return False
    return True


def simplicity(method, n: int, steps=10) -> bool:
    for i in range(steps):
        if not method(n):
            return False
    return True


def main():
    methods = [fermat, solovay_strassen, miller_rabin]

    for method in methods:
        print(method.__name__)
        for i in range(5, 150):
            if simplicity(method, i):
                print(i, end=' ')
        print('\n')


if __name__ == "__main__":
    main()
