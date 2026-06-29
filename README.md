# 🎓 Student Performance Predictor

A machine learning web application that predicts a student's **Mathematics Score** based on demographic and educational factors. This project demonstrates an end-to-end machine learning workflow, including data ingestion, preprocessing, model training, evaluation, and deployment using Flask.

---

## 🚀 Features

- 📥 Data Ingestion Pipeline
- 🔄 Data Transformation & Feature Engineering
- 🤖 Model Training with Multiple Regression Algorithms
- 📊 Automatic Model Selection
- 💾 Model Serialization using Pickle
- 🌐 Flask Web Application for Predictions
- 📝 Custom Logging and Exception Handling
- 🏗 Modular Project Structure following Software Engineering Best Practices

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Web Framework |
| Scikit-learn | Machine Learning |
| CatBoost | Gradient Boosting Model |
| XGBoost | Gradient Boosting Model |
| Pandas | Data Manipulation |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Pickle | Model Serialization |

---

## 📂 Project Structure

```text
mlproject/
│
├── app.py                    
├── application.py            
├── requirements.txt
├── setup.py
├── README.md
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── raw.csv
│
├── notebook/
│   └── EDA.ipynb
│
├── logs/
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── __init__.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   ├── utils.py
│   └── __init__.py
│
└── .gitignore
```

---

## 📊 Dataset

The project uses the **Students Performance in Exams** dataset.

### Features

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

### Target Variable

- Mathematics Score

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/dev-cherop/Student_Performance_predictor.git
```

### 2. Navigate to the project directory

```bash
cd Student_Performance_predictor
```

### 3. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train the model

```bash
python application.py
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## ⚙️ Machine Learning Workflow

```text
Dataset
    │
    ▼
Data Ingestion
    │
    ▼
Data Transformation
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
    │
    ▼
Model Evaluation
    │
    ▼
Best Model Selection
    │
    ▼
Model Serialization
    │
    ▼
Prediction Pipeline
    │
    ▼
Flask Web Application
```

---

## 🤖 Models Evaluated

The application compares multiple regression models to identify the best performer.

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- XGBoost Regressor
- CatBoost Regressor

The best-performing model is automatically selected and saved for prediction.

---

## 📈 Evaluation Metric

The regression models are evaluated using:

- R² Score

The model with the highest R² score is saved for inference.

---

## 📸 Application Preview

Add screenshots here after deployment.

```
screenshots/
├── home.png
├── prediction_form.png
└── prediction_result.png
```

Example:

```markdown
![Home Page](screenshots/home.png)

![Prediction Form](screenshots/prediction_form.png)

![Prediction Result](screenshots/prediction_result.png)
```

---

## 🔮 Future Improvements

- Deploy using Render or Railway
- Dockerize the application
- CI/CD with GitHub Actions
- Add REST API using FastAPI
- Model Explainability using SHAP
- Improve UI with Bootstrap or Tailwind CSS
- Hyperparameter Optimization
- User Authentication

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👤 Author

**Cherop**

Machine Learning Enthusiast | Python Developer

GitHub: https://github.com/dev-cherop

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork it
- 📢 Share it with others

Happy Coding! 🚀
