import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rf
from sklearn.externals import joblib
df = pd.read_csv("~/datasets/titanic/titanic_train.csv")

df_ohe = pd.get_dummies(df[['Age', 'Sex','Embarked', 'Survived' ]], columns=['Sex','Embarked'], dummy_na=True)
for col in df_ohe:
    df_ohe[col].fillna(0, inplace=True)
    
dependent_variable = 'Survived'
x = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
clf = rf()
clf.fit(x, y)

joblib.dump(clf, 'models/model.pkl')
model_columns = list(x.columns)
joblib.dump(model_columns, 'models/model_columns.pkl')
