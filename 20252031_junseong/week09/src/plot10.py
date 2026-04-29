import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 가로 9인치, 세로 4인치의 거대한 캔버스(Figure) 준비
plt.figure(figsize=(9, 4))

plt.subplot(2, 3, 1) # 2행 3열의 1번 방에 진입
plt.plot([1, 2], [1, 2])     # 1번 방에 선 그리기

plt.subplot(2, 3, 6) # 갑자기 2행 3열의 6번 방으로 이동
plt.plot([1, 2], [2, 1])     # 6번 방에 선 그리기

plt.show()  # 2, 3, 4, 5번 방은 텅 빈 채로 출력됩니다.