import numpy as np

print(np.sum([i for i in range(1000) if (i % 5 == 0) | (i % 3 == 0)]))