import numpy as np
mat = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)

# 총 요소(알맹이)의 개수
print("데이터 총 개수(size):", mat.size) 
# 결과: 6 (2 x 3)

# 메모리 차지 용량 (Bytes)
print("메모리 총 차지량(nbytes):", mat.nbytes)
# 결과: 48 (6개의 원소 x 각 8 bytes(int64) = 48 bytes)