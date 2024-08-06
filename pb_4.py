import numpy as np
from utils import monitor

def is_palidrome(n):
    s = str(n)
    return s == s[::-1]

@monitor
def largest_palindrome(d):
    find = False
    max_factor = int(''.join(['9']*d))
    max = max_factor ** 2
    for n in range(max, 1, -1):
        if is_palidrome(n):
            for i in range(max_factor, 10**(d-1), -1):
                find = (n % i == 0) & (10**(d-1) <= n // i < 10**d)
                if find:
                    break
            if find:
                break
    return f'{n} = {i} x {n // i}'

print(largest_palindrome(d=2))
