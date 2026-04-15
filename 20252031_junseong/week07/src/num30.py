import numpy as np

a = np.arange(1, 7)
print("원본 1차원 배열 a:\n", a)

a = a.reshape(2, 3)
print("원본 2차원 배열 a:\n", a)

print("평탄화 배열:", a.ravel())