import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 그래프 설정 (한글 폰트 및 마이너스 기호 깨짐 방지)
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
sns.set_palette("Set2") # 부드러운 파스텔톤 팔레트 적용

# Seaborn에 내장된 타이타닉 데이터셋 불러오기
df = sns.load_dataset('titanic')

# 처음 5개 행(Row) 확인
df.head()

# 1. 컬럼별 결측치 개수 확인
print("--- 정제 전 결측치 확인 ---")
print(df.isnull().sum())

# 2. 'deck' 컬럼은 결측치가 너무 많아(약 77%) 정보로서의 가치가 없으므로 삭제(Drop)
df = df.drop('deck', axis=1)

# 3. 'age' 컬럼의 결측치는 전체 승객 나이의 중앙값(Median)으로 채움(Imputation)
median_age = df['age'].median()
df['age'] = df['age'].fillna(median_age)

print("\n--- 정제 후 결측치 확인 ---")
print(df.isnull().sum())

# 1행 2열의 그래프 공간 생성 (크기는 가로 14, 세로 6)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 첫 번째 그래프: 성별 단순 탑승/생존자 '수' 비교 (Countplot)
sns.countplot(data=df, x='sex', hue='survived', ax=axes[0], palette=['#e74c3c', '#2ecc71'])
axes[0].set_title('성별 생존자 및 사망자 수 (Count)')
axes[0].set_xlabel('성별')
axes[0].set_ylabel('인원 수 (명)')
# 범례 이름 변경
axes[0].legend(['사망(0)', '생존(1)'])

# 두 번째 그래프: 객실 등급별 '평균 생존율' 비교 (Barplot)
sns.barplot(data=df, x='pclass', y='survived', ax=axes[1], palette='Blues_d')
axes[1].set_title('객실 등급별 생존율 (Survival Rate)')
axes[1].set_xlabel('객실 등급 (1=VIP)')
axes[1].set_ylabel('생존율 (%)')
# Y축을 0~1 (0%~100%) 로 고정하여 직관성 확보
axes[1].set_ylim(0, 1) 

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# X축은 생존 여부, Y축은 요금, 시각적 아름다움을 위해 박스플롯 적용
sns.boxplot(data=df, x='survived', y='fare', palette='Set3', linewidth=2)

# Y축에 로그(Log) 스케일을 적용하여 시각적 왜곡 줄이기
# 요금은 0달러부터 500달러까지 편차가 너무 커서 로그 변환을 하면 박스 모양을 선명하게 볼 수 있습니다.
plt.yscale('log')

plt.title('생존 여부에 따른 티켓 요금(Fare)의 분포 (Log Scale)')
plt.xlabel('생존 여부 (0 = 사망, 1 = 생존)')
plt.ylabel('티켓 요금 (Fare)')
plt.xticks([0, 1], ['사망자 그룹', '생존자 그룹']) # X축 눈금 이름 변경
plt.grid(True, axis='y', alpha=0.3)

plt.show()