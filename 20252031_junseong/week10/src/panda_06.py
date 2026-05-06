import pandas as pd

# 학생들의 성적 데이터 생성 (인덱스는 학생 이름)
st_names = ['희빈', '수영', '현수', '지호', '지민']
p = pd.Series([99, 84, 92, 65, 78], index=st_names)

# 명패 달아주기
p.name = '수학성적'
p.index.name = '이름'

print("--- 원본 데이터 ---")
print(p)

# 점수가 낮은 학생부터 (오름차순, 기본값)
print(p.sort_values())

# 점수가 높은 1등부터 (내림차순)
print(p.sort_values(ascending=False))

# 학생 이름(가나다) 순서로 정렬
print(p.sort_index())
