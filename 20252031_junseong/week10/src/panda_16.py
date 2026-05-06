import pandas as pd
# 1번 시리즈는 인덱스가 0, 1, 2
col_a = pd.Series([10, 20, 30], index=[0, 1, 2])
print(col_a)

# 2번 시리즈는 인덱스가 1, 2, 3 (0번이 없고 3번이 있음!)
col_b = pd.Series([3, 2, 1], index=[1, 2, 3])
print(col_b)

df_misaligned = pd.DataFrame({'A': col_a, 'B': col_b})

print("--- 엇갈린 인덱스의 병합 결과 ---")
print(df_misaligned)