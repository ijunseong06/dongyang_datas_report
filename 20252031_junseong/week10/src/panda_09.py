import pandas as pd
import numpy as np

# 1. 원시 재료 (3행 2열의 Numpy 배열)
raw_materials = np.array([[10, 20], [30, 40], [50, 60]])

# ----------------------------------------
# 케이스 A: 알아서 만들어줘! (기본값)
# ----------------------------------------
df_default = pd.DataFrame(data=raw_materials)

print("--- [A] 알아서 만들어진 표 (기본값) ---")
print(df_default)

# ----------------------------------------
# 케이스 B: 주문서에 상세 옵션 적기
# ----------------------------------------
df_custom = pd.DataFrame(
    data=raw_materials,
    index=['1일차', '2일차', '3일차'],  # 세로줄 이름 지정
    columns=['오전매출', '오후매출'],     # 가로줄 이름 지정
    dtype=float                         # 소수점으로 만들어줘!
)

print("\n--- [B] 상세 주문서가 적용된 표 ---")
print(df_custom)
