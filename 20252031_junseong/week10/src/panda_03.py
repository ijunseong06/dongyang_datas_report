import pandas as pd

# 1. 과일의 가격 데이터를 가지는 리스트 준비
prices = [1500, 3000, 2000, 500]

# 2. 각 데이터에 매칭될 이름표(Index) 준비
fruit_names = ["Apple", "Banana", "Orange", "Kiwi"]

# 3. Series 조립하기! (데이터명: '과일 단가표')
s = pd.Series(data=prices, index=fruit_names, name="과일 단가표")

print("🍎 판다스 Series 생성 완료:\n")
print(s)

# 내부 속성 훔쳐보기
print("\n--- 내부 구조 ---")
print("1) 값(values):", s.values)
print("2) 인덱스(index):", s.index)
print("3) 이름(name):", s.name)