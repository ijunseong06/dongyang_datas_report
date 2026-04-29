import koreanize_matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# 팁(tips) 데이터셋 소환!
tips = sns.load_dataset('tips')

plt.figure(figsize=(6, 4))
sns.set_theme(style="darkgrid") # 그래프 배경을 세련된 회색 모눈종이로 변경

# X축에는 청구 요금, Y축에는 팁을 지정하여 점 찍기
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', size='size', sizes=(20, 200), alpha=0.6)

plt.title("총 청구액과 팁의 관계")
plt.show()