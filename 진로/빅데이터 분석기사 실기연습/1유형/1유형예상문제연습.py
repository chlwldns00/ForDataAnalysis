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

#문제 9: 'vs' 컬럼의 데이터값중 10프로를 임의로 null값 처리후 이 null값을 다시 중앙값으로 대체후 해당 컬럼의 평균값을 정수로 출력
# null_fraction=0.2
# n_nulls=int(null_fraction*len(df))
# indices= np.random.choice(df.index,size=n_nulls,replace=False)
# print(type(indices))
# df.loc[indices,'vs']=np.nan

# df['vs'].fillna(df['vs'].median(),inplace=True)
# print(df['vs'].mean())

#문제10: 결측지가 포함된 열이름과 각 열의 결측지 갯수를 출력
missing_data=df.isnull().sum()
missing_data=missing_data[missing_data>0]
for col,count in missing_data.items():
			 print(f"{col}:{count}개 결측지 갯수")
# + 결측지 삭제
df.dropna()

# 정규화, min-max z-score등 코드보기 1유형 

# 해당 화면에서는 제출하지 않으며, 문제 풀이 후 답안제출에서 결괏값 제출