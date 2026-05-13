import pandas as pd

pf = pd.DataFrame(
    data=[
        [25, 35, 8, 18],
        [18, 27, 10, 20],
        [17, 17, 10, 19]
    ],
    index=['윤일형', '강수희', '홍소희'],
    columns=['중간', '기말', '과제', '출석']
)
print("--- 📚 원본 성적표 ---")
print(pf)

# 행은 "전부 다(:)", 열은 "'과제'" 만!
col_single = pf.loc[:, '과제']

print("--- [1단계] 전교생 과제 점수 (Series 반환) ---")
print(col_single)

# 행은 "전부 다(:)", 열은 "'중간'부터 '과제' 열까지 싹 다!"
col_sliced = pf.loc[:, '중간':'과제']

print("--- [2단계] 중간부터 과제까지 슬라이싱 ---")
print(col_sliced)

# 행은 "전부 다(:)", 열은 "['기말', '출석'] 만 핀셋으로 집어서!"
col_multi = pf.loc[:, ['기말', '출석']]

print("--- [3단계] 기말과 출석만 골라내기 ---")
print(col_multi)