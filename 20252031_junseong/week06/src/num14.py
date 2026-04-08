import numpy as np

a = np.arange(6)
print(a)

a = a.reshape(2, 3)
print(a)

b = np.full_like(a, [1, 2, 3])
print(b)