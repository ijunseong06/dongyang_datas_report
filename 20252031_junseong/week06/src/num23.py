import numpy as np

# 원소 4개가 차례대로 들어있는 1차원 배열: Shape (4,)
x = np.array([0, 10, 20, 30])
print("베이스 1차원 배열 x:", x)

# 행(row)은 원래 데이터 전부(:) 사용, 열(col) 자리를 빈 껍질(newaxis)로 쪼개어 세움!
# 1차원 (4,) 모델이 -> 2차원 (4, 1) 모델로 우뚝 섬!
x_tower = x[:, np.newaxis]

print("세로 기둥 탑으로 솟은 x_tower:\n", x_tower)
print("x_tower의 배열 구조(Shape):", x_tower.shape)