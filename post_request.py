import requests

url = "http://localhost:8008/predict"
data = {"text": "Ne mogu se prijaviti na svoj račun"}

response = requests.post(url, json=data)
result = response.json()["result"]

print(result)