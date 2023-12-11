import requests


url = "https://www.travel.taipei/open-api/zh-tw/Attractions/All?page=1"

response = requests.get(url, headers={"accept": "application/json"})
json_data = response.json()

for data in json_data["data"]:
    print(data["name"], data["address"])
