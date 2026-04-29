import koreanize_matplotlib
import matplotlib.pyplot as plt

# 1. 두 변수(X, Y) 데이터
heights = [160, 165, 170, 175, 180]
weights = [55, 60, 68, 70, 85]

# 2. 점 흩뿌리기
plt.scatter(heights, weights, color='red', s=100) # s는 점의 크기
plt.title('키와 몸무게의 선형 관계 (Scatter Plot)')
plt.show()