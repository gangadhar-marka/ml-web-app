import uvicorn
from fastapi import FastAPI
import joblib

app = FastAPI()

# Load the phishing model
phish_model = joblib.load('phishing.pkl')

@app.get('/')
def read_root():
    return {"message": "Welcome to the Phishing URL Checker"}

@app.get('/predict/')
async def predict(url: str):
    # Use your model to make predictions here
    y_Predict = phish_model.predict([url])

    if y_Predict[0] == 'bad':
        result = "This is a Phishing Site"
    else:
        result = "This is not a Phishing Site"

    return {"url": url, "result": result}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
