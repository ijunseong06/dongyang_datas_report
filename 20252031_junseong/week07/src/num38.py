import numpy as np

# [수평 결합용] 위아래 높이(행)가 똑같이 2층인 기차 화물칸 준비
A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[5, 6], 
              [7, 8]])

# [2단계] hstack으로 수평(Horizontal) 결합! 
# 주의!: 두 개의 배열을 튜플 괄호로 포장((A, B))하여 넘겨야 합니다.
train = np.hstack((A, B))

print("🚀 hstack 결합으로 쭈욱 길어진 기차:\n", train)