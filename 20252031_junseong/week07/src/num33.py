import numpy as np

# 원본 1차원 배열 생성
org = np.arange(5)
print("원본 org:", org)

# 원본의 거울(View) 생성
v = org.view()
print("뷰 v:", v)