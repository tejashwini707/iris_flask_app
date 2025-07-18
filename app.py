from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("svm_iris_model.pkl")
encoder = joblib.load("label_encoder.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        # Extract input values from form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Create input array for prediction
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Predict using the model
        prediction = model.predict(features)
        predicted_species = encoder.inverse_transform(prediction)[0]

        return render_template("index.html", result=f"The predicted Iris species is: {predicted_species}")
    
    except Exception as e:
        return render_template("index.html", result=f"Error: {e}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
