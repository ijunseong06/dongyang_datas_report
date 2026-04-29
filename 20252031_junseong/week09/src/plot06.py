import  koreanize_matplotlib
import matplotlib.pyplot as plt

labels = ['아이폰', '갤럭시', '기타']
sizes = [45, 50, 5] # 총합 비율

# 파이 나누기 (autopct: 퍼센트 출력 형식 지정)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('스마트폰 시장 점유율 (Pie Chart)')
plt.show()