# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

import pandas as pd

df = pd.read_csv("data/mtcars.csv")
#print(df.head(3))
# 사용자 코딩
#1번 : mpg 변수의 제 1사분위를 구하고 정수값으로 출력하시오.
# q1=df['mpg'].quantile(0.25)
# print(int(q1))

#2번:mpg값이 19이상 21이하인 데이터의 수를 구하시오
#print(len(df[(df['mpg']>=19) & (df['mpg']<=21)]))

# 해당 화면에서는 제출하지 않으며, 문제 풀이 후 답안제출에서 결괏값 제출