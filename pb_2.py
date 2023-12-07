import numpy as np
from utils import monitor

@monitor
def fibonacci_v1(max):
    fibonacci = [1]
    n = 2
    while n < max:
        fibonacci.append(n)
        n = np.sum(fibonacci[-2:])

    return np.sum([i for i in fibonacci if (i % 2 == 0)])

@monitor
def fibonacci_v2(max):
    n1, n2 = 1, 2
    sum = 0
    while n2 < max:
        if (n2 % 2) == 0:
            sum += n2
        n1, n2 = n2, n1+n2
    return sum


print(fibonacci_v1(4e6))
print(fibonacci_v2(4e6))