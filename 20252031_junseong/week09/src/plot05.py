import koreanize_matplotlib
import matplotlib.pyplot as plt

# 수많은 임의의 점수 데이터 분포
math_scores = [35, 60, 65, 65, 70, 75, 80, 85, 85, 90, 95]

# bins=5: 데이터를 5개 구간(통)으로 썰어서 개수를 세어라!
plt.hist(math_scores, bins=5, color='purple', edgecolor='black')
plt.title('수학 점수 밀집 분포 (Histogram)')
plt.show()