import numpy as np

# 0제곱부터 9제곱까지 10개의 숫자 생성
a = np.power(np.arange(10), 2)
print("베이스 1차원 배열 a:\n", a)

# 앞에서 4번째 데이터 (인덱스 3)
print("a[3]의 값:", a[3])

# 뒤에서 2번째 데이터 (인덱스 -2)
print("a[-2]의 값:", a[-2])