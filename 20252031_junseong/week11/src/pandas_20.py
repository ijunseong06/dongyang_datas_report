import pandas as pd

# 학생 5명의 성적 데이터프레임
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

print("--- 📚 원본 통합 성적표 ---")
print(pf)

# 대괄호 하나: 시리즈!
print(type(pf['기말']))          # Series 반환

# 대괄호 두 개: 데이터프레임!
df_single_col = pf[['기말']]
print(type(df_single_col))       # DataFrame 반환

print("\n--- 2차원 표로 유지된 기말고사 ---")
print(df_single_col)