import pandas as pd

courses = pd.Series(["Spark", "PySpark", "Hadoop"], name='과목명')
fees = pd.Series([250000, 300000, 200000], name='수강료')

print("--- 준비된 재료 (Series) ---")
print(courses)
print(fees)

# 시리즈가 원래 가진 name을 키 필드로 씁니다.
df_dict = pd.DataFrame({
    courses.name: courses, 
    fees.name: fees
})

print("--- [방법 1] 딕셔너리 바인딩 ---")
print(df_dict)