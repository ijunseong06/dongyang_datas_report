import numpy as np

org = np.arange(5)

# 독립된 클론(Copy) 생성
c = org.copy()

# 클론을 강제로 수정
c[2] = 200
print("변경된 복사본 c:", c)

# 보호된 원본 확인
print("안전한 원본 org:", org)