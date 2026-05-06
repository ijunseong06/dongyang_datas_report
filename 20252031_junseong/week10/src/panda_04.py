import pandas as pd

# 1. 원시 데이터 딕셔너리 준비 (Series들이 뭉쳐질 재료)
# {열 이름 : 리스트 데이터} 형태로 구성합니다.
raw_data = {
    "이름": ["Alice", "Bob", "Charlie", "Diana"],
    "나이": [25, 30, 35, 28],
    "직업": ["개발자", "디자이너", "기획자", "데이터분석가"],
    "연봉": [5000, 4800, 5200, 4500]
}

# 2. DataFrame 조립! 
# (행을 지칭할 Index를 문자열 'a', 'b', 'c', 'd'로 명시할 수도 있음)
df = pd.DataFrame(data=raw_data, index=['a', 'b', 'c', 'd'])

print("🏢 판다스 DataFrame 구성 완료:\n")
print(df)

print("\n--- 내부 구조 3종 세트 ---")
print("1) 열 목록(columns):", df.columns.tolist())
print("2) 행 주소(index):", df.index.tolist())
print("3) 순수 값(values):\n", df.values)