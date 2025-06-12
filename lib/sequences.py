#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    a, b = 0, 1

    for _ in range(length):
        fibonacci.append(a)
        a, b = b, a + b

    print(fibonacci)
