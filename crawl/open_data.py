import requests

url = "https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/1550/245aa5d2-c5b5-4e7d-afbf-420248f63e2c.json"

response = requests.get(url)
json_data = response.json()

for data in json_data:
    print(data["名稱"], data["地址"], data["電話"])
