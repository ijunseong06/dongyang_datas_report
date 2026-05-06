import pandas as pd

st_names = ['희빈', '수영', '현수', '지호', '지민']
p = pd.Series([99, 84, 92, 65, 78], index=st_names)

print("최고 점수 (max):", p.max())
print("최저 점수 (min):", p.min())
print("학급 평균 점수 (mean):", p.mean())
print("정중앙 중간값 (median):", p.median())
print("총 학생 수 (count):", p.count())