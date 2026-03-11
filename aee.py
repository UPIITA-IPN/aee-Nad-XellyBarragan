#!/usr/bin/env python3

import sys

def get_inverse(a, n):
    x0, x1 = 1, 0
    n_orig = n

    while n != 0:
        q = a // n
        a, n = n, a % n
        x0, x1 = x1, x0 - q * x1

    if a != 1:
        return None

    return x0 % n_orig


if __name__ == "__main__":
    # Usar argumentos si se pasan, sino leer desde stdin
    if len(sys.argv) >= 3:
        a, n = int(sys.argv[1]), int(sys.argv[2])
    else:
        a, n = map(int, input().split())

    inv = get_inverse(a, n)

    if inv is not None:
        print(inv)