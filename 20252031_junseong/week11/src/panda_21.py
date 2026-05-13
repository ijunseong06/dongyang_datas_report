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

# 질문: '중간' 점수가 20점 초과인가?
condition = pf['중간'] > 20

print("--- 질문에 대한 답안지 (True/False) ---")
print(condition)

# "중간 > 20" 인 학생만 남겨라!
df_filtered = pf[pf['중간'] > 20]

print("--- 필터링 완료된 데이터프레임 ---")
print(df_filtered)
