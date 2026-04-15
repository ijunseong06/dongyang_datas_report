import numpy as np

# 나만의 난수 생성 기계(Generator)를 'rg'라는 변수에 할당합니다.
# 괄호 안의 숫자(12345)는 '시드(seed)' 라고 부릅니다.
rg = np.random.default_rng(12345)

print("할당된 기계:", rg)