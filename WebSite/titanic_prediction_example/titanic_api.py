from flask import Flask, jsonify, request
from sklearn.externals import joblib
import pandas as pd
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get Parameters to DataFrame    
    json_ = request.form.to_dict()
    query_df = pd.DataFrame([json_])
    # data cleaning
    query = pd.get_dummies(query_df)
    model_columns = joblib.load('../models/model_columns.pkl')
    query = query.reindex(columns=model_columns, fill_value=0)
    for col in model_columns:
        if col not in query.columns:
            query[col] = 0
    # Pridicting
    prediction = clf.predict(query).tolist()
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    clf = joblib.load('../models/model.pkl')
    app.run(host="192.168.35.52",port=6666)
