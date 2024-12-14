from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from flask_cors import CORS

# Load the dataset with the correct encoding
df = pd.read_csv('spam.csv', encoding='ISO-8859-1')  # or 'latin1'

# Preprocessing the data
df['v1'] = df['v1'].map({'ham': 0, 'spam': 1})
X = df['v2']  # Email messages
y = df['v1']  # Labels (spam or ham)

# Convert text data into numerical data using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Create a Flask app
app = Flask(__name__)
CORS(app)

# API route to serve predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    message = data['message']  # Extract the message from the request
    vectorized_message = vectorizer.transform([message])  # Vectorize the input message
    prediction = model.predict(vectorized_message)[0]  # Make a prediction
    return jsonify({'prediction': 'spam' if prediction == 1 else 'ham'})  # Return the result

# API route for model evaluation metrics
@app.route('/metrics', methods=['GET'])
def metrics():
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred).tolist()  # Convert to list for JSON serialization
    classification_rep = classification_report(y_test, y_pred, output_dict=True)  # JSON-serializable classification report
    return jsonify({
        'accuracy': accuracy,
        'confusion_matrix': conf_matrix,
        'classification_report': classification_rep
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
