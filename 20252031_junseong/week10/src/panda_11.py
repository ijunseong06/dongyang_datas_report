import numpy as np
import pandas as pd

# 1. 0~11까지의 숫자를 3행 4열로 쪼갠 넘파이 배열 생성
np_array = np.arange(12).reshape(3, 4)

df_np = pd.DataFrame(data=np_array, columns=['Col1', 'Col2', 'Col3', 'Col4'])

print("--- NumPy 배열 기반 데이터프레임 ---")
print(df_np)