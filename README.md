# 🎓 Student Performance Predictor

A machine learning project that predicts a student's final grade (G3) based on demographic, social, and academic features from the UCI Student Performance dataset.

---

## 📌 Project Overview

Early identification of at-risk students can help educators intervene before it's too late. This project builds and compares multiple regression models to predict final student grades, and surfaces the key factors that influence academic performance.

---

## 🗂️ Project Structure

```
Student-Performance-Predictor/
│
├── Student_Performance_Predictor.ipynb   # Main analysis notebook
├── app.py                                # Streamlit web app
├── student-mat.csv                       # Dataset (download instructions below)
└── README.md
```

---

## 📊 Dataset

**Source:** [UCI Machine Learning Repository – Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance)

- 395 student records, 33 features
- Target variable: `G3` (final grade, scale 0–20)
- Key features: `G1`, `G2` (period grades), `studytime`, `failures`, `absences`, `Medu`, `Fedu` (parental education)

**To use the dataset:**
1. Download from the UCI link above
2. Unzip and place `student-mat.csv` in the project root folder
3. Update the file path in the notebook if needed

---

## 🔍 Notebook Walkthrough

The notebook covers the full data science workflow:

**1. Data Loading & Exploration**
- Load the dataset with the correct `;` separator
- Inspect shape, data types, and summary statistics

**2. Exploratory Data Analysis (EDA)**
- Distribution of final grades
- Correlation heatmap (numeric features only)
- Study time vs final grade (box plot)
- Past failures vs final grade (box plot)

**3. Preprocessing**
- Drop target column and separate features
- Encode categorical variables using `pd.get_dummies()`
- Train/test split (80/20)

**4. Model Training & Comparison**

| Model | MAE | R² |
|---|---|---|
| Linear Regression | ~1.8 | ~0.80 |
| Decision Tree | ~2.1 | ~0.75 |
| Random Forest | ~1.2 | ~0.87 |

Random Forest performed best across both metrics.

**5. Feature Importance**
- Top predictors: `G2`, `G1`, `failures`, `absences`
- Prior grades are by far the strongest signals

**6. Cross-Validation**
- 5-fold cross-validation on Random Forest
- Result: R² of ~0.85 ± 0.04, confirming the model generalizes well

**7. Prediction**
- Single student prediction compared against actual grade

---

## 🚀 Streamlit App

The app lets you interactively predict a student's final grade by adjusting inputs.

**Run locally:**

```bash
pip install streamlit
streamlit run app.py
```

**Inputs:**
- Study time (1–4 scale)
- Number of past failures
- Number of absences
- First period grade (G1)
- Second period grade (G2)

---

## 🛠️ Tech Stack

- **Python 3**
- **Pandas & NumPy** – data manipulation
- **Matplotlib & Seaborn** – visualization
- **Scikit-learn** – model training and evaluation
- **Streamlit** – web app deployment

---

## 💡 Key Insights

- A student's grades in earlier periods (G1, G2) are the strongest predictors of their final grade — much more than social or demographic factors.
- Past failures have a clear negative impact on final performance.
- Random Forest outperformed simpler models, likely due to its ability to capture non-linear relationships between features.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
pip install -r requirements.txt
```

**requirements.txt:**
```
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
```

---

## 👤 Author

**Your Name**  
[GitHub](https://github.com/your-username) • [LinkedIn](https://linkedin.com/in/your-profile)
