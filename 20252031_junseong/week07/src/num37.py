import numpy as np

x = np.arange(6)

# reshape()은 대표적으로 View를 반환하는 함수입니다!
y = x.reshape(2, 3) 
print("y의 본거지(base)는 누구냐?", y.base)

# Transpose 연산도 View를 반환합니다.
z = y.transpose()
print("z의 본거지(base)는 누구냐?", z.base)

# 명시적으로 Copy를 한 것은 본체가 자기 자신이므로 None이 나옵니다.
c = z.copy()
print("c의 본거지(base)는?", c.base)