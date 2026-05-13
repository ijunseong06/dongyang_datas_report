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

# pf.index[0] 은 '윤일형' 이라는 문자열을 반환합니다.
print("1번 타자 이름:", pf.index[0])

# 그 이름을 다시 loc 에게 전달합니다.
first_row = pf.loc[pf.index[0]]

print("\n--- 첫 번째 행 성적 (Series 반환) ---")
print(first_row)

# 1번 인덱스('강수희') 부터 4번 인덱스('신수빈') "전"까지의 명단을 가져옵니다.
range_names = pf.index[1:4]
print("뽑힌 명단:", range_names.tolist())

# 그 명단을 loc 에 통째로 집어넣습니다!
sliced_df = pf.loc[range_names]

print("\n--- 슬라이싱된 행 데이터프레임 ---")
print(sliced_df)

# 1. pf.loc[pf.index[1:4]] 로 학생 3명을 뽑고,
# 2. 뒤이어 [['기말', '과제']] 를 덧붙여 열을 필터링합니다.
final_df = pf.loc[pf.index[1:4]][['기말', '과제']]

print("--- 특정 행 + 특정 열 동시 추출 결과 ---")
print(final_df)
