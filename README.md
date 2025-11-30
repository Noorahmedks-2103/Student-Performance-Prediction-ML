# 🎓 Student Performance Prediction Using Machine Learning

This project predicts **Math Score** based on demographic and academic features using a **Linear Regression model**. It includes full Exploratory Data Analysis (EDA), visualization, model training, and performance evaluation.

---

## 📂 Project Files
├── StudentsPerformance.csv  
├── EDA.ipynb  
├── heatmap.png  
├── model.pkl  
└── src  
  └── model.py

---

## 📊 Exploratory Data Analysis (EDA)
Visual insights include:
- Score distributions (Math, Reading & Writing)
- Boxplot comparison of scores
- Impact of Lunch type & Test Preparation
- Gender comparison
- **Correlation Heatmap**

### 📈 Heatmap Example
![Heatmap](heatmap.png)

---

## 🤖 Machine Learning Model

### Algorithm Used
- **Linear Regression**
- Train-test split: **80 / 20**

### Model Performance
R2 Score: 0.88
MSE: 29.09

### Model Script
Located in: `src/model.py`

---

## 🚀 How to Run
```bash
git clone https://github.com/Noorahmedks-2103/Student-Performance-Prediction-ML.git
cd Student-Performance-Prediction-ML
pip install pandas numpy seaborn matplotlib scikit-learn
python src/model.py
Key Learnings

Data preprocessing & feature encoding

Exploratory Visualizations & Heatmaps

Regression modelling & evaluation metrics

Saving trained ML models with pickle

🌟 Future Enhancements

Add Random Forest & compare model performance

Deploy using Streamlit Web App

Create dashboard interface

👨‍💻 Developer

K S Noor Ahamad
📍 Tirupati, Andhra Pradesh
📧 nkurnipalli34@gmail.com

🔗 GitHub: https://github.com/Noorahmedks-2103

🔗 LinkedIn: https://www.linkedin.com/in/k-s-noor-ahmed-943403319

📜 License (MIT)
MIT License

Copyright (c) 2025 K S Noor Ahamad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software...

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...

