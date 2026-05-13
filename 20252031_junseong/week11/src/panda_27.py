import pandas as pd

pf = pd.DataFrame(
    data=[
        [25, 35, 8, 18],     # 0번 행
        [18, 27, 10, 20],    # 1번 행
        [17, 17, 10, 19]     # 2번 행
    ],
    index=['윤일형', '강수희', '홍소희'],     # 신경쓰지 마세요! iloc은 이름표를 무시합니다.
    columns=['중간', '기말', '과제', '출석'] # 여기도 신경쓰지 마세요!
)
print("--- 📚 원본 성적표 ---")
print(pf)

# 1. 1번 행 (두 번째 학생 '강수희') 참조
row_idx1 = pf.iloc[1]

# 2. 1번과 2번 행 뭉터기로 참조 (리스트로 묶기)
multi_rows = pf.iloc[[1, 2]]

print("--- [1] 인덱스 1번 행 (Series) ---")
print(row_idx1)

print("\n--- [2] 인덱스 1, 2번 행 (DataFrame) ---")
print(multi_rows)

# 모든 행(:) 가져오고, 열은 2번 인덱스('과제')만 가져오기
col_idx2 = pf.iloc[:, 2]

# 모든 행(:) 가져오고, 열은 1번('기말')부터 끝까지 슬라이싱!
sliced_cols = pf.iloc[:, 1:]

print("--- [1] 인덱스 2번 열 (과제) ---")
print(col_idx2)

print("\n--- [2] 1번 열부터 끝까지 슬라이싱 ---")
print(sliced_cols)

# 1번 행, 1번 열의 단일 데이터 (값 1개만 나옴)
scalar_val = pf.iloc[1, 1]

# 0번부터 2번 전(1번)까지 행 자르고,
# 1번부터 3번 전(2번)까지 열 자르기
sub_matrix = pf.iloc[0:2, 1:3]

print("--- [1] (1, 1) 단일 원소 ---")
print(scalar_val)

print("\n--- [2] 2차원 부분 데이터프레임 ---")
print(sub_matrix)


# 이름으로 한 칸 찾기 (loc의 초고속 버전)
fast_label = pf.at['강수희', '과제']

# 번호로 한 칸 찾기 (iloc의 초고속 버전)
fast_index = pf.iat[1, 2]

print("강수희 과제 점수 (.at) :", fast_label)
print("1행 2열 과제 점수 (.iat) :", fast_index)
