import numpy as np

# 동일 위치에 사칙연산을 먹이기 위한 배열 구성
c = np.array([1, 4, 9])
d = np.full_like(c, 2)  # 통일된 [2, 2, 2] 생성

# 1:1 요소별 연산을 Ufunc을 직접 호출하여 내부 엔진으로 수행
print("요소별 더하기 함수 np.add(c, d):", np.add(c, d))
print("요소별 거듭제곱 np.power(c, d):", np.power(c, d))  # c 안의 요소들을 d 값(2) 만큼 승수 적용(1^2, 4^2, 9^2)