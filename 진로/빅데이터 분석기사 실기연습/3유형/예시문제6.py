import pandas as pd

df = pd.read_csv("data/Titanic.csv")

#1.
# print(df[['Gender', 'Survived']].head(5))
crosstab = pd.crosstab(df['Gender'], df['Survived'])
print(crosstab)

from scipy.stats import chi2_contingency
print(chi2_contingency(crosstab))
# 260.717

#2.
print(df[['Gender', 'SibSp', 'Parch', 'Fare']].head(3))

from statsmodels.formula.api import logit

model = logit("Survived ~ C(Gender) + SibSp + Parch + Fare", data=df).fit()
print(model.summary())
print(round(-0.2007,3))
# -0.201

#3.
import numpy as np
print(model.params['SibSp'])
print(np.exp(model.params['SibSp']))

print(np.exp(-0.3539))
#0.702