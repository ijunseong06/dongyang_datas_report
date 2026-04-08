import numpy as np

# 거대한 3x3 배열 x는 기존과 동일하게 존재
x = np.arange(1, 10).reshape(3, 3)

# [1단계] 세로로 3층이 쌓인 (3, 1) 모양의 좁은 세로 기둥 배열 y (가로가 1칸으로 유연함)
y = np.array([[3], 
              [6], 
              [9]])
print("좁은 세로 기둥 y:\n", y)

# [2단계] 나누기 충돌! y가 구축해둔 허공(우측)으로 자신을 밀어내며 3x3을 위조!
result_col = x / y
print("\n✅ 세로 기둥 측면 브로드캐스팅 결과:\n", result_col)