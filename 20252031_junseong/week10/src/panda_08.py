import pandas as pd
import numpy as np

# 설문조사 데이터 느낌의 시리즈 (결측값 NaN과 None 포함)
# 1은 '매우 불만족', 6은 '매우 만족' 등을 나타낸다고 상상해봅시다.
s = pd.Series([3, 1, 1, 2, None, np.nan, 4, 6, 6, np.nan])

print("--- 원본 설문 데이터 ---")
print(s)

print(s.value_counts())

print(s.value_counts(dropna=False))