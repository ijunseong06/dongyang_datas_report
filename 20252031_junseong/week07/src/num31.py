import numpy as np

a = np.arange(1, 7).reshape(2, 3)
print("원본 2x3 배열:\n", a)

# 다음 3가지 방법은 모두 똑같이 2x3 배열을 3x2 배열로 단번에 뒤집습니다.
print("\nnp.transpose(a) 결과:\n", np.transpose(a))
print("\na.transpose() 결과:\n", a.transpose())
print("\na.T 속성 직접 접근 결과:\n", a.T)