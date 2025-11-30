import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

<<<<<<< HEAD
df = pd.read_csv("StudentsPerformance.csv")
df = df[["math score", "reading score", "writing score", "gender", "lunch", "test preparation course"]]
=======
# Load dataset
df = pd.read_csv("../StudentsPerformance.csv")

# Select only needed features
df = df[["math score", "reading score", "writing score", "gender", "lunch", "test preparation course"]]

# One hot encoding limited categories
>>>>>>> 08f98593859a43607692aa6eb3d27b18f32178f0
df = pd.get_dummies(df, drop_first=True)

print("Training columns:")
print(df.columns)

<<<<<<< HEAD
=======
# Split into X and y
>>>>>>> 08f98593859a43607692aa6eb3d27b18f32178f0
X = df.drop("math score", axis=1)
y = df["math score"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

<<<<<<< HEAD
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
=======
# Save the model
pickle.dump(model, open("model.pkl", "wb"))
>>>>>>> 08f98593859a43607692aa6eb3d27b18f32178f0

print("Model trained successfully. model.pkl saved.")
