import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("../StudentsPerformance.csv")

# Select only needed features
df = df[["math score", "reading score", "writing score", "gender", "lunch", "test preparation course"]]

# One hot encoding limited categories
df = pd.get_dummies(df, drop_first=True)

print("Training columns:")
print(df.columns)

# Split into X and y
X = df.drop("math score", axis=1)
y = df["math score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully. model.pkl saved.")
