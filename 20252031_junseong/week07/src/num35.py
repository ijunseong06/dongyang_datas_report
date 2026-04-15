import numpy as np

x = np.arange(8)

# 2칸 공간에 2개를 넣는 건 OK
x[3:5] = [30, 40]
print("동일 규격 교환:", x)

# 2칸밖에 없는 View 자리에 3개의 원소를 우겨넣으면?
# x[3:5] = [30, 40, 50]  --> ValueError: could not broadcast 에러 터짐!