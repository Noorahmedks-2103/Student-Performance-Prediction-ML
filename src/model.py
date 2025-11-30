import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("StudentsPerformance.csv")
df = df[["math score", "reading score", "writing score", "gender", "lunch", "test preparation course"]]
df = pd.get_dummies(df, drop_first=True)

print("Training columns:")
print(df.columns)

X = df.drop("math score", axis=1)
y = df["math score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully. model.pkl saved.")
