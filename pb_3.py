import numpy as np
from utils import monitor

@monitor
def generate_primes(n):
    """
    Very fast but memory inefficient
    """
    is_prime = np.ones(n, dtype=bool)
    is_prime[0:2] = False
    for i in range(int(n**0.5)):
        if is_prime[i]:
            is_prime[i*2::i] = False
    return np.where(is_prime)[0]

@monitor
def largest_prime_factor(n):
    """
    Rely on the factorized form
        n = f1 x f2 x ... x f3
    w/ f1 < f2 < .. < fn
    """
    largest_prime = n
    i = 2
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n = n // i 
        i = i + 1
    return n


# print(generate_primes(10**5))


print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
