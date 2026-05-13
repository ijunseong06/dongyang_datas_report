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

# pf.columns[0] 은 '중간' 이라는 문자열을 반환합니다.
print("첫 번째 열 이름:", pf.columns[0])

# 그 문자열을 loc의 두 번째 인자(열 자리)에 던집니다.
first_col = pf.loc[:, pf.columns[0]]

print("\n--- 첫 번째 과목 점수 (Series) ---")
print(first_col)

# 1번 인덱스('기말') 부터 끝까지의 컬럼명 명단을 가져옵니다.
col_slice = pf.columns[1:]
print("뽑힌 컬럼 명단:", col_slice.tolist())

# 뽑힌 명단을 냅다 loc에 집어넣습니다!
df_sliced_cols = pf.loc[:, col_slice]

print("\n--- 두 번째 과목부터 끝까지의 성적 ---")
print(df_sliced_cols)

# 1. 1~3번 학생의 모든 성적을 뽑는다 (pf.loc[pf.index[1:4]])
# 2. 거기서 '기말'과 '과제' 열만 살린다 ([['기말', '과제']])
chain_df = pf.loc[pf.index[1:4]][['기말', '과제']]

print("--- 우회 검색 체인 액션 결과 ---")
print(chain_df)