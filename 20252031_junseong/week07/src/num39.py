import numpy as np


# [수직 결합용] 가로 폭(열)이 똑같이 3칸 구역인 아파트 모듈 준비
C = np.array([[1, 2, 3]])
D = np.array([[4, 5, 6]])

# [3단계] vstack으로 수직(Vertical) 결합! 
# 위아래로 차곡차곡 건물을 올려 2층짜리 다세대 주택을 만듭니다.
apartment = np.vstack((C, D))

print("🏢 vstack 결합을 통해 완성된 번듯한 2층 아파트:\n", apartment)