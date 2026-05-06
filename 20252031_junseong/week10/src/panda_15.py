import pandas as pd
import json
import os

# JSON 파일 경로 설정
file_path = os.path.join(os.path.dirname(__file__), 'survey_data.json')

# 1. json 라이브러리를 사용하여 데이터를 읽어오는 방식
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
df_from_json = pd.DataFrame(data)

print("--- json.load()를 이용한 데이터 로드 ---")
print(df_from_json)
print("\n")

# 2. pandas의 read_json() 기능을 직접 사용하는 방식
df_direct = pd.read_json(file_path)

print("--- pd.read_json()을 이용한 직접 로드 ---")
print(df_direct)
