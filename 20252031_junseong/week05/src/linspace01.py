import numpy as np
import matplotlib.pyplot as plt

# 0부터 10까지의 구간을 100개의 점으로 매우 촘촘하게 쪼갭니다. (X축)
x = np.linspace(0, 10, 100)

# 100개의 x 좌표 각각에 대해 사인(Sine) 값을 계산합니다. (Y축)
y = np.sin(x)

# 계산된 100개의 (x, y) 좌표들을 선으로 연결하여 부드러운 곡선을 그립니다.
plt.plot(x, y)
plt.title("np.linspace()를 활용한 부드러운 사인 곡선")
plt.show()