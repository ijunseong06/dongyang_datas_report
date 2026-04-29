import koreanize_matplotlib
import matplotlib.pyplot as plt

# 1. 시계열(시간) 데이터 준비
years = [2020, 2021, 2022, 2023]
prices = [1000, 1500, 800, 2000]

# 2. 선 그리기
plt.plot(years, prices, color='blue', marker='o', linestyle='-')
plt.title('연도별 자산 가치 추세 (Line Plot)')
plt.show()