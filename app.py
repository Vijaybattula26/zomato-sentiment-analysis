from flask import Flask, request, render_template
import pickle
import os
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load model and vectorizer
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        review = request.form["review"]

        if not review.strip():
            return render_template("index.html", prediction="❗ Please enter a review to analyze.")

        transformed_review = vectorizer.transform([review])
        prediction = model.predict(transformed_review)[0]

        # Save prediction to CSV
        result = pd.DataFrame([[review, prediction]], columns=["review", "sentiment"])
        csv_path = os.path.join(os.getcwd(), "predictions.csv")

        if os.path.exists(csv_path):
            result.to_csv(csv_path, mode="a", header=False, index=False)
        else:
            result.to_csv(csv_path, index=False)

        return render_template("index.html", prediction=f"🔍 Sentiment: {prediction.capitalize()}")

# Run app
if __name__ == "__main__":
    app.run(debug=True)
