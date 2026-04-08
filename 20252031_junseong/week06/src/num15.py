import numpy as np

# 0부터 시작하는 3칸짜리 정수 배열 생성
a = np.arange(3)

# 생성된 기본 배열의 형태를 출력하여 확인
print("기본 배열 a:", a)

# 배열 a의 각 원소에 단일 숫자 2를 모두 더합니다.
result_add = a + 2
print(result_add)

# 배열 a의 각 원소에서 지정된 단일 숫자 2를 뺍니다.
result_sub = a - 2
print(result_sub)

# 배열 a의 모든 요소에 단일 숫자 2를 곱셈 처리합니다.
result_mul = a * 2
print(result_mul)

# 배열 a의 각 원소를 각각 단일 숫자 2로 나눕니다.
result_div = a / 2
print(result_div)