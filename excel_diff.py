import pandas as pd

# 엑셀 파일 읽기
df1 = pd.read_excel('result1.xlsx')
df2 = pd.read_excel('result2.xlsx')

# 두 데이터프레임 비교
diff = df1.compare(df2)

# 차이점 출력
print(diff)
