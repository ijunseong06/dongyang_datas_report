import numpy as np

# (2행 3열) 앞 행렬 데이터 준비
a = np.full((2, 3), [1, 2, 3])
print("행렬 a:\n", a)

# (3행 2열) 뒤 행렬 데이터 준비
b = np.full((3, 2), [2, 1])
print("\n행렬 b:\n", b)

# 직관적인 골뱅이 연산자 (파이썬 3.5 이후 지원)
result_ab = a @ b
print("행렬 a @ b 연산 결과:\n", result_ab)

# 순서를 바꿔 b를 앞으로, a를 뒤로 넘길 경우 완전 다른 세상이 열립니다!
result_ba = b.dot(a)
print("행렬 b @ a 연산 결과:\n", result_ba)