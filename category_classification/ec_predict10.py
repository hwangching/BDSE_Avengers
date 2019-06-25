#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import csv
import json
import jieba
import jieba.analyse
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from collections import Counter
from gensim.corpora.dictionary import Dictionary
from gensim.models.tfidfmodel import TfidfModel
import heapq
from sklearn.externals import joblib
import requests
import re
import json
import sys
import pandas as pd
from sklearn.externals import joblib

import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from pyquery import PyQuery as pq
import datetime
import re
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.form.to_dict()
    web =['{}'.format(json_['url'])]
    good_df = pd.DataFrame()
    
    
    category1,category2,name_list,platform,original_price,price_list,price_detail,sales_list,tag,detail_content,store_pickup,today = firstpg(web[0])
    
    good_df['category1'] = category1
    good_df['category2'] = category2
    good_df['name'] = name_list
    good_df['originalprice'] = original_price
    good_df['price'] = price_list  
    good_df['price_detail'] = price_detail

    good_df['sales'] = sales_list
    good_df['tag'] = tag
    good_df['detail_content']= detail_content
    good_df['store_pickup'] = store_pickup
    good_df['date'] = today

    good_df['category1'].astype('str')
    good_df['category2'].astype('str')
    good_df['name'].astype('str')
    good_df['tag'].astype('str')
        
        
        
    good_df['new_name'] = good_df['category1']+good_df['category2']+good_df['name']+good_df['tag']
    good_df['new_name'] = good_df['new_name'].apply(lambda x:x.replace(' ','').replace('(','').replace(')','').replace(',','').replace('|','').replace('/','').replace('[','').replace(']',''))
    print(good_df['new_name'])
    good_df['content_cutted'] = good_df['new_name'].apply(word_cut)
    global code_Tfidf
    code_Tfidf = Data_prepara()
    with open('dictionary.pickle', 'rb') as handle:
        dictionary = pickle.load(handle)
    content_cutted = pd.Series([dictionary.doc2bow(x) for x in good_df['content_cutted']])
    content_cutted2 = pd.Series(map( lambda x: list(map( lambda y: y[0] ,x)),content_cutted))
    testX = model(content_cutted2)
    test_pred_label = clf.predict_proba(testX)
    google_id_dict = dic()
    d = dict()
    tp1 = dict()
    tp2 = dict()
    tp3 = dict()
    tp4 = dict()
    tp5 = dict()
    tp6 = dict()
    tp7 = dict()
    tp8 = dict()
    tp9 = dict()
    tp10 = dict()
    tp11 = dict()
    tp12 = dict()
    tp13 = dict()
    tp14 = dict()
    tp15 = dict()
    tp16 = dict()
    tp17 = dict()
    tp18 = dict()
    tp19 = dict()
    tp20 = dict()
    tp21 = dict()
    tp22 = dict()
    tp23 = dict()
    tp24 = dict()
    tp25 = dict()
    tp26 = dict()
    tp27 = dict()
    tp28 = dict()
    tp29 = dict()
    tp30 = dict()
    max_num_index_list = list(map(test_pred_label[0].tolist().index, heapq.nlargest(30, test_pred_label[0].tolist())))

    d['platform'] = platform
    d['product_name'] = good_df['name'][0]
    for j in range(0,30):
        if j ==0:
            tp1[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
            d['type_predict'] = google_id_dict[str(clf.classes_[max_num_index_list[j]])]
        elif j==1:
            tp2[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==2:
            tp3[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==3:
            tp4[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==4:
            tp5[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==5:
            tp6[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==6:
            tp7[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==7:
            tp8[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==8:
            tp9[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==9:
            tp10[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==10:
            tp11[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==11:
            tp12[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==12:
            tp13[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==13:
            tp14[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==14:
            tp15[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==15:
            tp16[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==16:
            tp17[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==17:
            tp18[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==18:
            tp19[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==19:
            tp20[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==20:
            tp21[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==21:
            tp22[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==22:
            tp23[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==23:
            tp24[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==24:
            tp25[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==25:
            tp26[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==26:
            tp27[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==27:
            tp28[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        elif j==28:
            tp29[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
        else :
            tp30[google_id_dict[str(clf.classes_[max_num_index_list[j]])]] = str(test_pred_label[0][max_num_index_list[j]])
    
    
    
    
    code=int(clf.classes_[max_num_index_list[0]])
    title=good_df['name'][0]
    unit_price=float(good_df['price'][0].replace('$',''))
    orig_unit_price=float(good_df['originalprice'][0].replace('$',''))


    
    
    enable_isp=int(good_df['store_pickup'] [0])
    subtotal=predictsales(code,title,unit_price,orig_unit_price,enable_isp)
    
    d['type_classify_ratio'] = [tp1,tp2,tp3,tp4,tp5,
                                tp6,tp7,tp8,tp9,tp10,
                                tp11,tp12,tp13,tp14,tp15,
                                tp16,tp17,tp18,tp19,tp20,
                                tp21,tp22,tp23,tp24,tp25,
                                tp26,tp27,tp28,tp29,tp30]

    d['sales_7days_predict'] =str(subtotal['pred_7days'].values[0])
    d['sales_14days_predict'] =str(subtotal['pred_14days'].values[0])
    d['sales_30days_predict'] =str(subtotal['pred_30days'].values[0])
    d['sales_60days_predict'] =str(subtotal['pred_60days'].values[0])
    d['sales_180days_predict'] = str(subtotal['pred_180days'].values[0])
    d['sales_total_predict'] = str(subtotal['pred_totalguid'].values[0])
    d['product_name']=d['product_name'].encode('utf-8').decode('utf-8')
 
    
    
    with open('result.json', 'w') as fp:
        json.dump(d, fp)
#     result = pd.DataFrame.from_dict(d)
#     result = pd.DataFrame(d)
#     result.to_csv('0624API.csv',encoding="utf_8_sig")
    return (jsonify(d))
def predictsales(code,title,unit_price,orig_unit_price,enable_isp):  
    import pandas as pd
    import numpy as np
    import jieba
    from jieba import analyse
    import jieba.analyse
    hotword_dict=pd.read_csv('keyword.csv')
    code_dict=pd.read_csv("code_api.csv")
    keywords=[]
    for i in hotword_dict.values.tolist():
        keywords.append(i[0])
    def word(w):
        lst = list(jieba.cut(w,cut_all=False))
        c=0
        for i in lst:
            if i in keywords:
                c+=1
            return(c)
    table=code_dict[code_dict.code==code]
    table['hottimes']=word(title)
    table['installment_3months']=0
    table['installment_6months']=0
    table['installment_12months']=0
    table['product_launch_month']=4
    table['product_launch_hour']=12
    table['product_launch_weekday']=4
    table['is_Presales']=0
    table['product_launch_year']=2019
    table['is_Longtern']=0
    table['is_Discount']=0
    table['unit_price']=unit_price
    table['orig_unit_price']=orig_unit_price
    table['enable_isp']=enable_isp
    table['price_gap']=table['orig_unit_price']-table['unit_price']
    table['compare_cate_unit_price']=table['unit_price']/table['category_unit_price']
    table=table[['unit_price', 'orig_unit_price', 'enable_isp', 'hottimes',
           'installment_3months', 'installment_6months', 'installment_12months',
           'product_launch_month', 'product_launch_hour', 'product_launch_weekday',
           'is_Presales', 'product_launch_year', 'is_Longtern',
           'category_unit_price', 'compare_cate_unit_price', 'is_Discount',
           'code_before14days_mean', 'code_before180days_mean',
           'code_before30days_mean', 'code_before60days_mean',
           'code_before7days_mean', 'code_before14days_median',
           'code_before180days_median', 'code_before30days_median',
           'code_before60days_median', 'code_before7days_median',
           'code_before14days_max', 'code_before180days_max',
           'code_before30days_max', 'code_before60days_max',
           'code_before7days_max', 'code_before14days_min',
           'code_before180days_min', 'code_before30days_min',
           'code_before60days_min', 'code_before7days_min', 'code_mean_7days',
           'code_max_7days', 'code_min_7days', 'code_median_7days',
           'code_mean_14days', 'code_max_14days', 'code_min_14days',
           'code_median_14days', 'code_mean_30days', 'code_max_30days',
           'code_min_30days', 'code_median_30days', 'code_mean_60days',
           'code_max_60days', 'code_min_60days', 'code_median_60days',
           'code_mean_180days', 'code_max_180days', 'code_min_180days',
           'code_median_180days', 'parent_code_mean_7days',
           'parent_code_max_7days', 'parent_code_min_7days',
           'parent_code_median_7days', 'parent_code_mean_14days',
           'parent_code_max_14days', 'parent_code_min_14days',
           'parent_code_median_14days', 'parent_code_mean_30days',
           'parent_code_max_30days', 'parent_code_min_30days',
           'parent_code_median_30days', 'parent_code_mean_60days',
           'parent_code_max_60days', 'parent_code_min_60days',
           'parent_code_median_60days', 'parent_code_mean_180days',
           'parent_code_max_180days', 'parent_code_min_180days',
           'parent_code_median_180days', 'parent_code_counts', 'code_counts',
           'price_gap']]
    concol=['unit_price', 'category_unit_price', 'compare_cate_unit_price', 
           'hottimes','code_before14days_mean', 'code_before180days_mean',
           'code_before30days_mean', 'code_before60days_mean',
           'code_before7days_mean', 'code_before14days_median',
           'code_before180days_median', 'code_before30days_median',
           'code_before60days_median', 'code_before7days_median',
           'code_before14days_max', 'code_before180days_max',
           'code_before30days_max', 'code_before60days_max',
           'code_before7days_max', 'code_before14days_min',
           'code_before180days_min', 'code_before30days_min',
           'code_before60days_min', 'code_before7days_min', 'code_mean_7days',
           'code_max_7days', 'code_min_7days', 'code_median_7days',
           'code_mean_14days', 'code_max_14days', 'code_min_14days',
           'code_median_14days', 'code_mean_30days', 'code_max_30days',
           'code_min_30days', 'code_median_30days', 'code_mean_60days',
           'code_max_60days', 'code_min_60days', 'code_median_60days',
           'code_mean_180days', 'code_max_180days', 'code_min_180days',
           'code_median_180days', 'parent_code_mean_7days',
           'parent_code_max_7days', 'parent_code_min_7days',
           'parent_code_median_7days', 'parent_code_mean_14days',
           'parent_code_max_14days', 'parent_code_min_14days',
           'parent_code_median_14days', 'parent_code_mean_30days',
           'parent_code_max_30days', 'parent_code_min_30days',
           'parent_code_median_30days', 'parent_code_mean_60days',
           'parent_code_max_60days', 'parent_code_min_60days',
           'parent_code_median_60days', 'parent_code_mean_180days',
           'parent_code_max_180days', 'parent_code_min_180days',
           'parent_code_median_180days', 'parent_code_counts', 'code_counts',
           'orig_unit_price']
    table[concol]=np.log1p(table[concol])
    import os
    os.environ['KMP_DUPLICATE_LIB_OK']='True'
    import xgboost as xgb
    import pickle #pickle模块
    #读取Model
    with open('xgb.pickle', 'rb') as f:
        xgb = pickle.load(f)
        #测试读取后的Model
    y_predict=xgb.predict(table)
    for i in y_predict:
        i.sort()
    subtotal=pd.DataFrame()
    subtotal['pred_7days']=np.expm1(np.array(y_predict))[:,0]
    subtotal['pred_14days']=np.expm1(np.array(y_predict))[:,1]
    subtotal['pred_30days']=np.expm1(np.array(y_predict))[:,2]
    subtotal['pred_60days']=np.expm1(np.array(y_predict))[:,3]
    subtotal['pred_180days']=np.expm1(np.array(y_predict))[:,4]
    subtotal['pred_totalguid']=np.expm1(np.array(y_predict))[:,5]
    def trans(x):
        if(x<0):
            return 0
        elif((x/unit_price)<1):
            return unit_price*100
        else:
            return(round(x/unit_price)*unit_price*100)
           
    subtotal['pred_7days']=subtotal['pred_7days'].apply(lambda x: round(x)).apply(trans)
    subtotal['pred_14days']=subtotal['pred_14days'].apply(lambda x: round(x)).apply(trans)
    subtotal['pred_30days']=subtotal['pred_30days'].apply(lambda x: round(x)).apply(trans)
    subtotal['pred_60days']=subtotal['pred_60days'].apply(lambda x: round(x)).apply(trans)
    subtotal['pred_180days']=subtotal['pred_180days'].apply(lambda x: round(x)).apply(trans)
    subtotal['pred_totalguid']=subtotal['pred_totalguid'].apply(lambda x: round(x)).apply(trans)
    return(subtotal)
      
    
def firstpg(web):    
    
    today = datetime.date.today()
    price_list = []
    price_detail = []
    name_list = []
    
    sales_list = []
    store_pickup = []
    original_price = []
    
   
    
    tag1 = ''
    tag = []
    category1 = []
    category2 = []
    detail_content = []
    url = web
   

    if 'pchome' in url:
        web1 = url[32:] 
        url = 'https://mall.pchome.com.tw/ecapi/ecshop/prodapi/v2/prod/'+web1+'-000&fields=Seq,Id,Name,Nick,Store,PreOrdDate,SpeOrdDate,Price,Discount,Pic,Weight,ISBN,Qty,Bonus,isBig,isSpec,isCombine,isDiy,isRecyclable,isCarrier,isMedical,isBigCart,isSnapUp,isDescAndIntroSync,isFoodContents,isHuge,isEnergySubsidy,isPrimeOnly,isWarranty,isLegalStore,isOnSale,isPriceTask&_callback=jsonp_prod&1561109220?_callback=jsonp_prod'
        

        url1 = url
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' #偽裝使用者
        headers = {'User-Agent':user_agent,
                      'server': 'PChome/1.0.4',
                      'Referer': 'https://mall.pchome.com.tw/newarrival/'}
        res = requests.get(url=url1,headers=headers)
        res_text = res.text
        res_text_format = res_text.replace('try{jsonp_prod(','').replace(');}catch(e){if(window.console){console.log(e);}}','')
        jd = json.loads(res_text_format)
        psku = web1+'-000'
        prdt = jd[psku]
        pcname = prdt['Name']
        oriprice = prdt['Price']['M']
        oriprice = '$'+str(oriprice)
        listprice = prdt['Price']['P']
        listprice = '$'+str(listprice)

        name_list.append(pcname)
        original_price.append(oriprice)
        price_list.append(listprice)
        
        
        category1 = ['']
        category2 = ['']
        price_detail = '一箱12包$420(平均每包$35)，99折後$416'
        sales_list = 5
        tag = ['']
        detail_content = [[]]
        store_pickup = [0]
        platform = 'pchome'
        return category1,category2,name_list,platform,original_price,price_list,price_detail,sales_list,tag,detail_content,store_pickup,today
    
    else:
        platform = '生活市集'

        user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' #偽裝使用者
        headers = {'User-Agent':user_agent,
                       'server': 'PChome/1.0.4',
                       'Referer': 'https://mall.pchome.com.tw/newarrival/'}
        res = requests.get(url=url,headers=headers)
        res_text = res.text
        d2 = pq(res_text)




        price_list_info = d2(".big-price").text()
        price_list.append(price_list_info) 
        name_list_info = d2("#item-main-content .title").text()
        name_list.append(name_list_info) 
        original_price_info = d2("del").text()
        original_price.append(original_price_info)
        sales_list_info = d2(".sale-count .site-color").text()
        sales_list.append(sales_list_info)


        if "可超商取" in re.split(r'[\n,買,\s,]',d2(".caption").text()):
            store_pickup.append(1) 
        else:
            store_pickup.append(0) 



        category1info = d2(".crumb").text().split()[0]
        category1.append(category1info)
        category2info = d2(".crumb").text().split()[1]
        category2.append(category2info)  

        detail_content_info  = d2(".detail-info p:nth-child(1)").text().split('\n')[1:] 
        detail_content.append(detail_content_info)

        price_detail_info = d2("#detail-content h4").text()
        price_detail.append(price_detail_info)

        for t in d2("#detail-content .item-tag.grey-444").items():    
            tag1 = tag1+t.text()

        print('.')

        tag.append(tag1)
        tag1 = ''
    

    return category1,category2,name_list,platform,original_price,price_list,price_detail,sales_list,tag,detail_content,store_pickup,today
    
def word_cut(mytext):
    return list(jieba.cut(mytext))
def dic():
    with open('google-id-dict2.pickle', 'rb') as handle:
        google_id_dict = pickle.load(handle)
    return google_id_dict
def Data_prepara():
    csv.field_size_limit(int(sys.maxsize/10000000000))
    df2=pd.read_csv('特徵資料.csv', engine='python',encoding='utf_8_sig')
    df3 = df2['tokens'].apply(lambda x :x.replace('[','').replace(']','').split(','))
    code_tokenGyTfidfSort4 =list(map( lambda x : list(map(toInt,x)) ,df3))
    return code_tokenGyTfidfSort4
def toInt(x):
    return int(x.strip())
def word(x):
    stroke = []
    for i in range(0,len(code_Tfidf)):    
        stroke.append(len(set(x)&set(code_Tfidf[i])))
    return(stroke)
def model(x):
    AA = []
    AA.append(list(x.apply(word)))
    df_AA = pd.DataFrame(AA[0])
    return df_AA

if __name__ == '__main__':
    clf = joblib.load("分類RandomForest_train_model.pkl")
    app.run(host="192.168.35.51",port=6678)


# In[ ]:




