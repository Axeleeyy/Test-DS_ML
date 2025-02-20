import requests

data = {
    "data" : [2000,200,3,0,0,0,0,234,159,1300,0,20]
}

response = requests.post("http://127.0.0.1:8000/predict/", json=data)
print(response.json())