from flask import Flask, jsonify, request
from sklearn.externals import joblib
import pandas as pd
app = Flask(__name__)

@app.route('/ec_predict_all', methods=['POST'])
def predict():
    return jsonify([      
    {
        "platform":"PChome",
        "product_name":"iPhone Xs",
        "type_predict":"Mobile Phones",
        "url":"https://24h.pchome.com.tw/prod/DXAO43-A900A0GPG",
        "sales_7days_predict":500000,
        "sales_14days_predict":700000,
        "sales_30days_predict":800000,
        "sales_60days_predict":900000,
        "sales_180days_predict":950000,
        "sales_total_predict":1000000
    },
    {
        "platform":"PChome",
        "product_name":"iPhone Xs",
        "type_predict":"Mobile Phones",
        "url":"https://www.buy123.com.tw/site/sku/2036751?cid=177313",
        "sales_7days_predict":500000,
        "sales_14days_predict":700000,
        "sales_30days_predict":800000,
        "sales_60days_predict":900000,
        "sales_180days_predict":950000,
        "sales_total_predict":1000000
    },
    {
        "platform":"PChome",
        "product_name":"iPhone Xs",
        "type_predict":"Mobile Phones",
        "url":"https://24h.pchome.com.tw/prod/DXAO43-A900A0GPG",
        "sales_7days_predict":500000,
        "sales_14days_predict":700000,
        "sales_30days_predict":800000,
        "sales_60days_predict":900000,
        "sales_180days_predict":950000,
        "sales_total_predict":1000000
    },
    {
        "platform":"PChome",
        "product_name":"iPhone Xs",
        "type_predict":"Mobile Phones",
        "url":"https://www.buy123.com.tw/site/sku/2036751?cid=177313",
        "sales_7days_predict":500000,
        "sales_14days_predict":700000,
        "sales_30days_predict":800000,
        "sales_60days_predict":900000,
        "sales_180days_predict":950000,
        "sales_total_predict":1000000
    },
    {
        "platform":"PChome",
        "product_name":"iPhone Xs",
        "type_predict":"Mobile Phones",
        "url":"https://24h.pchome.com.tw/prod/DXAO43-A900A0GPG",
        "sales_7days_predict":500000,
        "sales_14days_predict":700000,
        "sales_30days_predict":800000,
        "sales_60days_predict":900000,
        "sales_180days_predict":950000,
        "sales_total_predict":1000000
    }
    ])

if __name__ == '__main__':
    #clf = joblib.load('../models/model.pkl')
    app.run(host="192.168.35.51",port=9528)

