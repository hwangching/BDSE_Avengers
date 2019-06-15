from flask import Flask, jsonify, request
from sklearn.externals import joblib
import pandas as pd
app = Flask(__name__)

@app.route('/ec_predict', methods=['POST'])
def predict():
    # Get Parameters to DataFrame    
    json_ = request.form.to_dict()
    #query_df = pd.DataFrame([json_])
    # data cleaning
    #query = pd.get_dummies(query_df)
    #model_columns = joblib.load('../models/model_columns.pkl')
    #query = query.reindex(columns=model_columns, fill_value=0)
    #for col in model_columns:
    #    if col not in query.columns:
    #        query[col] = 0
    # Pridicting
    #prediction = clf.predict(query).tolist()
    #return jsonify({'prediction': prediction})
    return jsonify({
        'platform':'PChome',
        'product_name':'iPhone Xs',
        'type_predict':'Mobile Phones',
        'type_classify_ratio':
        {
            'Mobile Phones':0.6,
            'Tablet':0.2,
            'Telephone':0.1,
            'Headphone':0.05,
            'Camera':0.03,
            'GPS_Tracker':0.02
        },
        'sales_7days_predict':500000,
        'sales_30days_predict':800000,
        'sales_90days_predict':900000,
        'sales_total_predict':1000000
    })

if __name__ == '__main__':
    #clf = joblib.load('../models/model.pkl')
    app.run(host="192.168.35.52",port=9527)

