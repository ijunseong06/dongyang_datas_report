import pandas as pd

# 3행 3열짜리 2차원 리스트
data_2d = [
    [1, 2, 3],
    [10, 20, 30],
    [100, 200, 300]
]

# 데이터와 함께 index 이름표 지정
df_2d = pd.DataFrame(data=data_2d, index=list('abc'))

print("--- 2차원 리스트 + 행 인덱스 지정 ---")
print(df_2d)

df_full = pd.DataFrame(
    data=data_2d, 
    index=['1번방', '2번방', '3번방'], 
    columns=['A타입', 'B타입', 'C타입']
)

print("--- 완벽하게 라벨링된 표 ---")
print(df_full)

print("\n[현재 세팅된 이름표 확인]")
print("행 이름:", df_full.index.tolist())
print("열 이름:", df_full.columns.tolist())