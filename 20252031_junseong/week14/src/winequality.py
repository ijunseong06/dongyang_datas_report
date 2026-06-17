import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 그래프 설정
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
sns.set_palette("Set2")

# 로컬 CSV 파일 불러오기 (상대 경로 사용)
df = pd.read_csv('./20252031_junseong/week14/data/winequality.csv')

# 데이터 구조 및 첫 5행 확인
print(df.info())
df.head()

# 1. 모든 변수 간의 상관계수(-1.0 ~ 1.0)를 계산합니다.
correlation_matrix = df.corr()

# 2. 그중 우리가 궁금한 'quality' 컬럼만 쏙 뽑아서 내림차순 정렬합니다.
quality_corr = correlation_matrix['quality'].sort_values(ascending=False)

print("--- 와인 품질(Quality)과 가장 상관관계가 높은 성분들 ---")
print(quality_corr)

plt.figure(figsize=(8, 5))

# 타겟 변수의 빈도수를 막대그래프로 시각화
sns.countplot(data=df, x='quality', palette='viridis')

plt.title('와인 품질 점수(Quality) 분포', fontsize=16)
plt.xlabel('품질 등급 (3점~8점)')
plt.ylabel('데이터 개수 (병)')
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()

plt.figure(figsize=(10, 6))

# X축은 범주형(품질 등급), Y축은 연속형(알코올 도수)을 두어 Boxplot을 그립니다.
sns.boxplot(data=df, x='quality', y='alcohol', palette='coolwarm')

plt.title('와인 품질 등급별 알코올 도수 분포', fontsize=16)
plt.xlabel('품질 등급 (Quality)')
plt.ylabel('알코올 도수 (%)')
plt.grid(True, axis='y', alpha=0.3)

plt.show()