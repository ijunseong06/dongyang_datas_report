import koreanize_matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn을 통한 막대그래프: x는 범주, y는 수치
teams = ['A팀', 'B팀', 'C팀']
scores = [85, 92, 78]

sns.barplot(x=teams, y=scores, palette='viridis')
plt.title('부서별 평가 점수 비교 (Bar Chart)')
plt.show()
