import pandas as pd

pf = pd.DataFrame(
    data=[
        [25, 35, 8, 18],
        [18, 27, 10, 20],
        [17, 17, 10, 19],
        [12, 22, 9, 20],
        [22, 34, 8, 16]
    ],
    index=['윤일형', '강수희', '홍소희', '유한빈', '신수빈'],
    columns=['중간', '기말', '과제', '출석']
)
print("--- 📚 원본 성적표 ---")
print(pf)

# 가로 타겟: '윤일형', 세로 타겟: '출석'
target_score = pf.loc['윤일형', '출석']

print("--- [1단계] 단일 칸 조준 추출 ---")
print("윤일형 학생의 출석 점수:", target_score)
print("반환된 타입:", type(target_score))


# 가로 타겟: '윤일형'부터 '유한빈'까지 (4명)
# 세로 타겟: '기말' (1과목)
col_series = pf.loc['윤일형':'유한빈', '기말']

print("--- [2단계] 행 슬라이스 + 단일 열 추출 ---")
print(col_series)

# 가로(행) 타겟: '윤일형' 부터 '유한빈' 까지 
# 세로(열) 타겟: '기말' 부터 '과제' 까지
sub_matrix = pf.loc['윤일형':'유한빈', '기말':'과제']

print("--- [3단계] 작아진 형태의 부분 데이터프레임 ---")
print(sub_matrix)

# 행은 0번 학생부터 2번 학생까지! (파이썬 기본 슬라이싱이라 마지막 3번은 제외됨!) 
# 열은 2번째 과목('과제') 부터 끝까지!
dynamic_sliced = pf.loc[pf.index[0:3], pf.columns[2:]]

print("--- [4단계] 배열 번호를 활용한 동적 슬라이싱 ---")
print(dynamic_sliced)