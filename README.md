# 🎓 Student Performance Prediction — Machine Learning Project

This project predicts a student's **Math score** based on academic performance and study behavior.  
The model uses Linear Regression and achieves **88% accuracy (R² Score)**.

---

## 📌 Project Overview

| Category | Details |
|----------|---------|
| Problem Type | Regression (Numeric Prediction) |
| Algorithm Used | Linear Regression |
| Evaluation Metrics | R² Score, MSE |
| Score Achieved | **0.88 R²**, **29.09 MSE** |
| Tools Used | Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn |

---

## 📊 Dataset Information

Dataset used: `StudentsPerformance.csv`  
After feature selection & encoding, the final model uses:

#### **Input Features:**
- Reading Score
- Writing Score
- Gender (male / female)
- Lunch (standard / free)
- Test preparation course (none / completed)

#### **Target Output:**
- Math Score

---

## 🧠 Model Workflow

1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Selection
4. Encoding categorical variables
5. Train-Test Split (80/20)
6. Linear Regression Training
7. Model Evaluation Metrics
8. Saving model as `model.pkl`

---

## 🚀 How to Run the Project

### 🔽 Clone the Repository
```bash
git clone https://github.com/Noorahmedks-2103/Student-Performance-Prediction-ML.git
cd Student-Performance-Prediction-ML
