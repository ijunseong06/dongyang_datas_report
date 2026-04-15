import numpy as np

# 0.0 부터 8.0 까지 9개의 원소가 있는 1차원 배열
x = np.arange(9.0)
print("원본 배열 x:", x)

# x를 정확히 3등분 합니다.
s = np.split(x, 3)

print("\n🔪 3등분 결과:", s)
print("데이터 타입:", type(s))  # 결괏값이 리스트(List)형 태임에 주목하세요!
print("첫 번째 조각:", s[0])