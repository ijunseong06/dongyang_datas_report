import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 그래프 설정
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
sns.set_palette("colorblind")

# 로컬 CSV 파일 불러오기 (상대 경로)
df = pd.read_csv('./20252031_junseong/week14/data/bike_sharing.csv')

# 데이터 구조 및 첫 5행 확인
print(df.info())
df.head()

# 1. 텍스트(Object)로 된 날짜를 진짜 Datetime(시간 객체)으로 변환
df['date'] = pd.to_datetime(df['date'])

# 2. 요일을 숫자로 추출 (0: 월요일 ~ 6: 일요일)
df['day_of_week'] = df['date'].dt.dayofweek

# 3. 람다(lambda) 함수를 이용해 5,6(토,일)이면 '주말', 아니면 '평일'이라는 글자를 입력
df['is_weekend'] = df['day_of_week'].apply(lambda x: '주말' if x >= 5 else '평일')

# 마법이 성공했는지 샘플 확인
df[['date', 'day_of_week', 'is_weekend', 'count']].sample(5)

plt.figure(figsize=(10, 6))

# X축은 기온(temp), Y축은 대여량(count)
# scatter_kws: 점의 투명도(alpha)와 색상 조절
# line_kws: 회귀선의 두께와 색상 조절
sns.regplot(data=df, x='temp', y='count', 
            scatter_kws={'alpha': 0.4, 'color': 'steelblue'},
            line_kws={'color': 'crimson', 'linewidth': 3})

plt.title('기온(Temp) 상승에 따른 자전거 대여량 증가 폭 (회귀선)', fontsize=16)
plt.xlabel('평균 기온 (Celsius)')
plt.ylabel('총 대여량 (Count)')
plt.grid(True, linestyle=':', alpha=0.7)

plt.show()

plt.figure(figsize=(10, 6))

# 봄, 여름, 가을, 겨울의 논리적인 시간 순서를 리스트로 정의
season_order = ['Spring', 'Summer', 'Fall', 'Winter']

# 계절별 대여량 박스플롯 (order 파라미터로 순서 강제)
sns.boxplot(data=df, x='season', y='count', order=season_order, palette='Set2')

plt.title('계절(Season)이 자전거 대여 수요에 미치는 절대적 영향력', fontsize=16)
plt.xlabel('계절 (Season)')
plt.ylabel('총 대여량 (Count)')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()