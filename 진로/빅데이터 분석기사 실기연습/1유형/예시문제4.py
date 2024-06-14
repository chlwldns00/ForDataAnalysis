# 문제정의
# roc-auc -> 확률값을 예측 predict_proba()
# 양성(1, 남자) 클래스 확률값 
# 분류(이진)

# 데이터 불러오기
import pandas as pd
train = pd.read_csv("data/customer_train.csv")
test = pd.read_csv("data/customer_test.csv")

# EDA
pd.set_option('display.max_columns', None)
# print(train.shape, test.shape)
# print(train.head())
# print(train.info())
# print(train.isnull().sum())
# print(test.isnull().sum())

# 전처리
train['환불금액'] = train['환불금액'].fillna(0)
test['환불금액'] = test['환불금액'].fillna(0)

cols = ['회원ID', '총구매액', '최대구매액', '환불금액', '방문일수', '방문당구매건수', '주말방문비율', '구매주기']
target = train.pop('성별')

# 모델 학습 및 예측
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(train[cols], target)
pred = model.predict_proba(test[cols])
print(pred)
print(pred[:,1])

# 제출 
submit = pd.DataFrame({
	'pred': pred[:,1]
})

submit.to_csv('result.csv', index=False)

print(pd.read_csv('result.csv'))