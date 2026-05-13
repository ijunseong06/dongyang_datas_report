import pandas as pd

# 일부러 5월, 1월, 3월 순서로 데이터를 생성했습니다.
df = pd.DataFrame(
    data=[
        [239, 13, 522],
        [192, 5, 387],
        [216, 7, 419],
        [217, 7, 435]
    ],
    index=['2016년5월', '2016년1월', '2016년4월', '2016년3월'],
    columns=['사고(건)', '사망(명)', '부상(명)']
)

print("--- 📚 뒤죽박죽 원본 표 ---")
print(df)

# 행 인덱스 문자열 순서('1월' -> '3월' -> '5월')로 오름차순 정렬
# (기본값이 오름차순 ascending=True 로 작동합니다)
sorted_by_idx = df.sort_index()

# 만약 역순(최신순 등)으로 정렬하고 싶다면 ascending=False 를 줍니다.
reverse_idx = df.sort_index(ascending=False)

print("--- [1단계] 인덱스(날짜) 순서로 바르게 정렬 ---")
print(sorted_by_idx)

# '사고(건)' 의 숫자가 가장 작은 달부터 위에서 아래로 세웁니다.
sorted_by_val = df.sort_values(by='사고(건)')

# '사망' 숫자가 숫자가 가장 "큰" 달부터 (내림차순) 세웁니다.
highest_death = df.sort_values(by='사망(명)', ascending=False)

print("--- [2단계] 사고가 적은 순(오름차순)으로 줄 세우기 ---")
print(sorted_by_val)

# 동점자 처리: 사망자 수로 먼저 줄을 세우되, 
# 만약 사망자 수가 같다면 부상자 수로 다시 줄 세우기!
tie_breaker = df.sort_values(by=['사망(명)', '부상(명)'])

print("--- [3단계] 복합 기준(다중 열) 정렬 ---")
print(tie_breaker)