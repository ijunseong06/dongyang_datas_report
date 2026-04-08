import numpy as np

# [1, 4, 9] 실수형 배열 생성
b = np.array([1, 4, 9])
print("원본 배열 b:", b)

# 수학 엔진으로 각 숫자에 일괄 루트(Square Root)를 씌움! (for문 불필요)
result_sqrt = np.sqrt(b)
print("각 원소 루트 씌우기:", result_sqrt)

# 일괄 자연 로그(Log) 변환 적용. (데이터 그래프 분포를 부드럽게 펼칠 때 유용)
result_log = np.log(b)
print("자연 로그 변환:", result_log)