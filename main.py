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


