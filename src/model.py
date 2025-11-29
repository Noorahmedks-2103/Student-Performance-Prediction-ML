import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import pickle

# Load dataset
df = pd.read_csv("../StudentsPerformance.csv")

# Convert categorical values to numerical (encoding)
df = pd.get_dummies(df, drop_first=True)

# Split dataset
X = df.drop("math score", axis=1)
y = df["math score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
print("R2 Score:", r2_score(y_test, predictions))
print("MSE:", mean_squared_error(y_test, predictions))

# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as model.pkl")
