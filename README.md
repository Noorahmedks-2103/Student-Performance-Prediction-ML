# Student Performance Prediction — ML Project

**What is this?**  
This project predicts a student’s **Math score** based on reading/writing scores, gender, lunch type, and test-preparation status using a Linear Regression model.

---

## 📊 Data & Features  
- Dataset: `StudentsPerformance.csv`  
- Selected features:  
  - reading score  
  - writing score  
  - gender (male/female)  
  - lunch type (standard / free-reduced)  
  - test preparation course (none / completed)  
- Target: `math score`  

---

## 🧠 Model Training & Performance  
- Algorithm: Linear Regression  
- R² Score: ~ **0.88**  
- Mean Squared Error (MSE): ~ **29.1**  

---

## 🛠 How to run  
```bash
git clone https://github.com/Noorahmedks-2103/Student-Performance-Prediction-ML.git
cd Student-Performance-Prediction-ML
pip install -r requirements.txt   # (optional, to install dependencies)
python src/model.py               # trains model & saves model.pkl
