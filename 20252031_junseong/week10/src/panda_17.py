import pandas as pd
import numpy as np

# 임의의 데이터 딕셔너리
data_dict = {
    '이름': ['Alice', 'Bob'],
    '나이': [25, 30],
    '키': [165.5, 178.2]
}

df = pd.DataFrame(data=data_dict)

print("--- 원본 데이터프레임 ---")
print(df)

# 각 열의 보관함 규격 확인하기!
print("\n--- 열별 자료형(dtypes) 확인 ---")
print(df.dtypes)