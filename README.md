# 🌸 Iris Flower Classification - Flask Web App

This project is built as part of my **Data Science Internship at Codsoft**.  
It is a machine learning web application that predicts the species of an Iris flower (Setosa, Versicolor, Virginica) based on user input for four flower features using a **Support Vector Machine (SVM)** model.
-----------------------------------------
## 🚀 Project Overview

- **Model Used**: Support Vector Machine (SVM)
- **Language**: Python
- **Libraries**: Flask, scikit-learn, pandas, numpy, seaborn, matplotlib
- **Deployment**: [Render](https://render.com/)
- **Interface**: HTML (Jinja2 template)
-----------------------------------------
## 🔍 Problem Statement

The goal of this project is to classify Iris flower species based on input measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The model was trained on the **Iris dataset**, evaluated for accuracy, and deployed as a Flask-based web application.
-----------------------------------------
## 📊 Dataset Information

- **Source**: UCI Machine Learning Repository
- **Classes**: Iris-setosa, Iris-versicolor, Iris-virginica
- **Features**:
  - sepal_length
  - sepal_width
  - petal_length
  - petal_width
----------------------------------------
## 🧠 Model Training

- **Model**: `SVC` (Support Vector Classification)
- **Accuracy**: ~97%
- **Preprocessing**:
  - Label encoding
  - Train-test split (70-30)
- **Evaluation**: Classification report, confusion matrix
----------------------------------------
## 💡 Features of the App

- Predicts flower species from user input
- Displays prediction with species name
- Clean and minimal UI using HTML & CSS
- Hosted and accessible publicly
----------------------------------------
## 📁 Project Structure

iris_flask_app/
│
├── app.py # Flask application
├── requirements.txt # Dependencies
├── svm_iris_model.pkl # Trained SVM model
├── label_encoder.pkl # Label encoder for decoding predictions
├── templates/
│ └── index.html # Web form interface
└── render.yaml # Render deployment configuration
----------------------------------------
## 🌐 Live Demo

🔗 [Click to open the live app](https://iris-flask-app-1.onrender.com/)
----------------------------------------
## 🛠️ How to Run Locally:
1. Clone this repository  
   `git clone https://github.com/yourusername/iris_flask_app.git`

2. Navigate to the folder  
   `cd iris_flask_app`

3. Install dependencies  
   `pip install -r requirements.txt`

4. Run the Flask app  
   `python app.py`

5. Open `http://127.0.0.1:5000/` in your browser
---------------------------------------
## 📜 Acknowledgements

- Dataset from [kaggle](https://www.kaggle.com/datasets/arshid/iris-flower-dataset)
- Flask documentation
- render.com for deployment
- Codsoft Internship task guidelines
---------------------------------------
## 🧑‍💻 Developed By

**Tejashwini P R**  
B.E. Computer Science & Engineering  
Codsoft Data Science Intern (2025)  
[GitHub](https://github.com/tejashwini707)
