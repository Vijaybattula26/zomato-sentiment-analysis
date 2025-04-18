# 🍽️ Zomato Review Sentiment Analysis Web App

This is a full-stack sentiment analysis project that classifies Zomato reviews as **Positive**, **Negative**, or **Neutral**. Built using **Python, Flask, HTML, CSS**, and **machine learning models** trained on real-world Zomato review data.

---

## 🔍 Project Overview

This project covers:
- ✅ Data preprocessing and cleaning using NLP techniques
- ✅ Sentiment analysis using TextBlob & ML models
- ✅ Model training and evaluation (Logistic Regression, TF-IDF)
- ✅ Frontend (HTML + Bootstrap) + Flask backend
- ✅ Saving predictions to CSV
- ✅ Deployment-ready structure for GitHub or cloud hosting

---

## 📁 Project Structure

```bash
zomato-sentiment-app/
│
├── app.py                       # Flask application
├── index.html                   # Frontend template
├── model.pkl                    # Trained ML model (Logistic Regression)
├── vectorizer.pkl               # TF-IDF vectorizer
├── predictions.csv              # Stores user inputs and predictions
├── zomato_sentiment_analysis.ipynb  # Colab notebook (model training)
├── requirements.txt             # Required Python packages
└── README.md                    # You're here :)

📊 How the Model Works
Preprocessing

Lowercasing

Removing punctuation

Removing stopwords with NLTK

Sentiment Scoring
Using TextBlob polarity to label:

Positive: polarity > 0

Neutral: polarity = 0

Negative: polarity < 0

Vectorization

TfidfVectorizer with bigrams and stopword removal

Model Training

Logistic Regression

Alternatives: RandomForest, XGBoost, MultinomialNB

🌐 Web App Interface
The app is built with:

📜 Flask (Python backend)

🎨 Bootstrap for styling

😃 Emoji-based sentiment display

💾 CSV export of predictions

🚀 How to Run Locally
Clone the repository

bash
Copy
Edit
git clone https://github.com/Vijaybattula26/zomato-sentiment-analysis.git
cd zomato-sentiment-analysis
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app

bash
Copy
Edit
python app.py
Open http://127.0.0.1:5000 in your browser

🧠 Future Improvements
Integrate database (e.g., SQLite or MongoDB)

Add charts for analytics

Deploy on Render, Heroku, or AWS

Include login/signup authentication

🧑‍💻 Author & Portfolio Links
Vijay Battula

🔗 GitHub

💼 LinkedIn

💡 LeetCode

📸 Instagram

📜 License
MIT License. Use freely for learning or projects.

yaml
Copy
Edit

---

Let me know if you'd like a banner or screenshots included in the `README.md` too!
