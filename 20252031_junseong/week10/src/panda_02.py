import pandas as pd
import numpy as np

# 100만 개의 행과 3개의 열을 가진 무작위 데이터 생성
data = pd.DataFrame(np.random.rand(1000000, 3), columns=['A_Score', 'B_Score', 'C_Score'])

# 상위 3개 행만 출력하여 데이터 확인
print("100만 건 데이터 맛보기:\n", data.head(1000))
