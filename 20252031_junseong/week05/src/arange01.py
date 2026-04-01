import numpy as np

# 0부터 3 미만(2)까지, 기본 간격(step=1)으로 배열 생성
print(np.arange(3))

# 3부터 7 미만(6)까지, 기본 간격(step=1)으로 배열 생성
print(np.arange(3, 7))

# 3부터 7 미만(6)까지, 간격(step=2)을 두고 2칸씩 점프하여 생성
print(np.arange(3, 7, 2))