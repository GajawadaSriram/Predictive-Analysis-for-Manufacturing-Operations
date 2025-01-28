from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

app = Flask(__name__)

model = None
data = None

@app.route('/', methods=['GET'])
def load_home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_data():
    file = request.files.get('file')

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    global data
    data = pd.read_csv(file)

    return jsonify({"message": "File uploaded successfully", "stat": 1, "columns": list(data.columns)})

@app.route('/train', methods=['POST'])
def train_model():
    global model, data

    if data is None:
        return jsonify({"error": "No data uploaded"}), 400

    if 'Downtime_Flag' not in data.columns:
        return jsonify({"error": "'Downtime_Flag' column is missing in the dataset"}), 400

    data = data.dropna(subset=['Downtime_Flag'])
    data = data.dropna(axis=1, how='any')

    X = data.drop(columns=['Downtime_Flag'])
    y = data['Downtime_Flag']

    feature_columns = X.columns.tolist()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='binary')

    return jsonify({"message": "Model trained successfully", "accuracy": accuracy, "f1_score": f1})

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({"error": "Model not trained"}), 400

    input_data = request.get_json()
    input_df = pd.DataFrame([input_data])

    expected_columns = ['Machine_ID', 'Temperature', 'Run_Time']
    
    for column in expected_columns:
        if column not in input_df.columns:
            input_df[column] = [0]

    input_df = input_df[expected_columns]

    if 'Downtime_Flag' in input_df.columns:
        input_df = input_df.drop(columns=['Downtime_Flag'])

    prediction = model.predict(input_df)[0]
    confidence = max(model.predict_proba(input_df)[0])

    return jsonify({"Downtime": "Yes" if prediction else "No", "Confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True)
