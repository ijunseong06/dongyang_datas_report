import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(5, 5))

df = sns.load_dataset('titanic')
class_counts = df['pclass'].value_counts()
print(class_counts)

# 1. 파이 차트 먼저 그리기
plt.pie(class_counts, labels=['3rd', '1st', '2nd'], autopct='%.1f%%', colors=['#FFCCBC', '#C5CAE9', '#C8E6C9'])

# 2. 하얀색 원(도넛 구멍)을 만들어 도화지 한가운데 좌표(0,0)에 올리기
centre_circle = plt.Circle((0,0), 0.60, fc='white')
fig = plt.gcf() # 현재 도화지 가져오기
fig.gca().add_artist(centre_circle) # 도화지에 구멍 원 그리기

plt.title("모던한 도넛 차트 (Donut Chart)")
plt.show()