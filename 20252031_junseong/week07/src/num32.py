import numpy as np

# (3, 2, 2) 모양의 3차원 배열
b = np.arange(1, 13).reshape(3, 2, 2)

# 기본 전치 연산 (원래 (0, 1, 2) 였던 3차원 축을 (2, 1, 0) 역순으로 완전 반전)
print("3차원 배열 기본 전치(b.T):\n", b.T)

# 축 순서를 세밀하게 직접 제어 (깊이 0축과 열 2축만 서로 맞바꿈)
print("\nnp.transpose(b, (0, 2, 1)) 결과:\n", np.transpose(b, (0, 2, 1)))