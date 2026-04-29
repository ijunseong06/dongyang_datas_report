from pydataset import data 

# 함수의 인자를 비워두면, 제공하는 전체 데이터셋 목록표가 DataFrame으로 나옵니다.
all_data = data()
print(all_data.head())