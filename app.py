from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__)

# Load the phishing model
phish_model = joblib.load('phishing.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_phishing', methods=['POST'])
def check_phishing():
    # Get the URL entered by the user from the form
    url = request.form.get('url')

    # Use your model to make predictions here
    prediction = phish_model.predict([url])[0]  # Assuming the model takes a list of URLs

    # Determine the result message
    if prediction == 'bad':
        result = "This is a Phishing Site"
    else:
        result = "This is not a Phishing Site"

    # Reset the form fields by redirecting back to the index page
    return render_template('result.html', user_url=url, result=result)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
