import pandas as pd

# '열 제목' : [세로줄에 들어갈 데이터 목록] 형태로 딕셔너리를 만듭니다.
data_dict = {
    'numbers': [1, 2, 3], 
    'colors': ['red', 'white', 'blue']
}

df = pd.DataFrame(data_dict)

print("--- 딕셔너리로 생성한 표 ---")
print(df)

print("열 이름표 (Columns):", df.columns)
print("행 이름표 (Index):", df.index)

import pandas as pd

# 학생 3명의 국어, 수학 점수 데이터
score_dict = {
    '국어': [82, 76, 67], 
    '수학': [99, 87, 78]
}

# 딕셔너리를 넘기면서, 어느 학생의 점수인지 행 인덱스를 달아줍니다.
df_scores = pd.DataFrame(
    data=score_dict, 
    index=['김국진', '신영희', '이길순']
)

print("--- 행 인덱스까지 완벽하게 지정된 성적표 ---")
print(df_scores)