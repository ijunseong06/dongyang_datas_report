import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic' # 윈도우는 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 전체 도화지 준비
fig = plt.figure(figsize=(8, 6))

# 1. 3행 3열짜리 모눈종이(GridSpec)를 하나 도화지 위해 투명하게 선언합니다.
gs = GridSpec(3, 3)

# 2. 첫째 행(row=0), 모든 열(col=:)을 차지하는 거대한 서브플롯 추가
ax1 = fig.add_subplot(gs[0, :])
ax1.set_title("ax1: gs[0, :]")
ax1.plot([1, 2, 3], [10, 20, 30], color='red')

# 3. 2~3행(row=1:), 1~2열(col=:2)을 차지하는 정사각형 서브플롯 추가
ax2 = fig.add_subplot(gs[1:, :2])
ax2.set_title("ax2: gs[1:, :2]")
ax2.scatter([1, 2, 3], [3, 2, 1], color='green', s=100)

# 4. 2~3행(row=1:), 마지막 열(col=2)을 차지하는 세로로 긴 서브플롯 추가
ax3 = fig.add_subplot(gs[1:, 2])
ax3.set_title("ax3: gs[1:, 2]")
ax3.bar(['A', 'B'], [5, 10], color='orange')

# 레이아웃 정리 및 출력
plt.tight_layout()
plt.show()