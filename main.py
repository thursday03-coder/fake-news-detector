import pandas as pd
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")
fake ["label"] = 1
true ["label"] = 0
data = pd.concat([fake , true])
data = data.sample(frac=1)
print(data.head())
X = data ["text"]
y = data ["label"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(len(data))
print(len(X_train))
print(len(X_test))


