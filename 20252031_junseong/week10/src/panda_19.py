import pandas as pd
import numpy as np

# 1. 2025년 3월 2일부터 6일간의 연속된 날짜를 생성
dates = pd.date_range(start="20250302", periods=6)

print("--- 준비된 캘린더 축 (Index) ---")
print(dates)

# 2. 넘파이 난수(표준정규분포)를 이용해 6행 4열짜리 변동성 데이터 생성
# (날짜가 6일이므로, 행의 개수를 반드시 6으로 맞춰야 조립됩니다!)
random_data = np.random.randn(6, 4)

# 3. 데이터, 날짜 축(index), 컬럼명(columns)을 모아서 데이터프레임 합체!
df_time = pd.DataFrame(
    data=random_data, 
    index=dates,                 # 위에서 만든 시간축을 좌측 인덱스에 삽입!
    columns=list("ABCD")         # ['A', 'B', 'C', 'D'] 로 컬럼명 지정
)

print("\n🏢 완성된 시계열 데이터프레임:\n")
print(df_time)

import matplotlib.pyplot as plt

# A열과 B열의 날짜별 변화 추이 그리기
df_time[['A', 'B']].plot(title="Time Series Trend", figsize=(8,4))
plt.show()