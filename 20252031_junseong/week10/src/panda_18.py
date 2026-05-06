import pandas as pd

# 2025년 1월 1일 연속된 6일의 날짜를 생성합니다.
dates = pd.date_range(start="20250101", periods=6)

print("--- 6일치 기본 날짜 생성 ---")
print(dates)

dates_by_end = pd.date_range(start="20250101", end='20250110')
print("\n--- 1월 1일부터 10일까지 ---")
print(dates_by_end)

import pandas as pd
# 3일 간격으로 6번 반복
dates_3d = pd.date_range("2025-01-01", periods=6, freq='3D')
print("--- 3일 간격 생성 ---")
print(dates_3d)

# 3시간 간격으로 6번 반복 (시간 개념 추가!)
dates_3h = pd.date_range("2025-01-01", periods=6, freq='3h')
print("\n--- 3시간 간격 생성 ---")
print(dates_3h)

import pandas as pd
# 2025년 1월 1일 이후 다가오는 첫 화요일부터 4번 생성을 시작합니다.
tuesdays = pd.date_range("2025-01-01", periods=4, freq='W-TUE')

print("--- 다가오는 화요일 연속 4주 ---")
print(tuesdays)

# 월 말일 (월급날 결산용)
month_ends = pd.date_range("2025-01-01", periods=3, freq='ME')
print("--- 매월 말일 3번 ---")
print(month_ends)

# 월 초일 (월별 새로운 시작용)
month_starts = pd.date_range("2025-01-01", periods=3, freq='MS')
print("\n--- 매월 1일 3번 ---")
print(month_starts)