import pandas as pd
import numpy as np

# 리스트로 생성 (np.nan은 결측값/빈 값을 의미합니다)
s = pd.Series([1, 3, 5, np.nan, 6, 8], name='first')
print(s)