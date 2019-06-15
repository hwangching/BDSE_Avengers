import requests
import pandas as pd

url = 'http://bdse52:6666/predict'
data = {'Age':77, 'Embarked':'S', 'Sex':'male'}

response = requests.post(url, data=data)
response.json()
