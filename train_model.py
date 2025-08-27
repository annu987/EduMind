# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Sample data (you can replace this with a CSV dataset)
data = {
    'study_hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'attendance': [60, 65, 70, 75, 80, 85, 90, 95],
    'participation': [3, 4, 5, 5, 6, 7, 8, 9],
    'result': [0, 0, 0, 1, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
}

df = pd.DataFrame(data)

X = df[['study_hours', 'attendance', 'participation']]
y = df['result']

model = LogisticRegression()
model.fit(X, y)

# Save model
with open('model/predictor.pkl', 'wb') as file:
    pickle.dump(model, file)
print("✅ Model trained and saved!")