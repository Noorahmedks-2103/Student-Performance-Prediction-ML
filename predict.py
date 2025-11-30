import pickle
import pandas as pd

# Load dataset to get all original feature columns after encoding
df = pd.read_csv("StudentsPerformance.csv")
df = pd.get_dummies(df, drop_first=True)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Create an empty row with all model feature columns initialized as 0
input_df = pd.DataFrame(columns=df.drop("math score", axis=1).columns)
input_df.loc[0] = 0

# ------------ SAMPLE INPUT VALUES -------------
input_df.at[0, "reading score"] = 85
input_df.at[0, "writing score"] = 82
input_df.at[0, "gender_male"] = 1
input_df.at[0, "lunch_standard"] = 1
input_df.at[0, "test preparation course_none"] = 1
# ------------------------------------------------

# Predict
prediction = model.predict(input_df)[0]
print(f"Predicted Math Score: {round(prediction)}")
