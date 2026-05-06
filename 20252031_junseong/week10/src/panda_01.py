import pandas as pd

# 1. 딕셔너리를 활용하여 데이터 준비
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 92, 78, 95]
}

# 2. DataFrame으로 변환 및 출력
df = pd.DataFrame(data)

print("--- 원본 데이터 ---")
print(df)

# 3. 데이터 필터링: Score가 90을 초과하는 우수 학생만 추출
excellent_students = df[df['Score'] > 90]

print("\n--- 90점 초과 우수 학생 ---")
print(excellent_students)