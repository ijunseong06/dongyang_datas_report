import numpy as np

# 3행 2열짜리 학생 성적표 자료(배열) 생성
a = np.array([[10, 20], 
              [ 5,  8], 
              [ 1,  2]])
print("원본 배열 a:\n", a)

# 배열 안의 모든 숫자를 영혼까지 끌어모아 통째로 더하기
total_sum = a.sum()
print("전체 원소의 합:", total_sum)

# 세로 방향(과목별)으로 누적 합계 내기
col_sum = a.sum(axis=0)
print("세로 압축(axis=0) 결과:", col_sum)