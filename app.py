from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model/predictor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    study_hours = float(request.form['study_hours'])
    attendance = float(request.form['attendance'])
    participation = float(request.form['participation'])

    prediction = model.predict([[study_hours, attendance, participation]])[0]
    result = "🎉 Pass" if prediction == 1 else "❌ Fail"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
