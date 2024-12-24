from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the saved model and vectorizer
model = joblib.load('model/random_forest_model.joblib')
tfidf_vectorizer = joblib.load('model/tfidf_vectorizer.joblib')

# In-memory storage for review statistics
review_data = {
    'total_reviews': 0,
    'fake_reviews': 0,
    'real_reviews': 0
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html', stats=review_data)

@app.route('/submit_review')
def review_form():
    return render_template('review_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    review_vectorized = tfidf_vectorizer.transform([review])
    prediction = model.predict(review_vectorized)
    result = 'real' if prediction == 0 else 'fake'

    # Update review statistics
    review_data['total_reviews'] += 1
    if result == 'fake':
        review_data['fake_reviews'] += 1
    else:
        review_data['real_reviews'] += 1

    gif = 'happy.gif' if result == 'real' else 'sad.gif'
    return render_template('result.html', prediction=result, gif=gif)

if __name__ == '__main__':
    app.run(debug=True)



