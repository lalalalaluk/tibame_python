import json
import requests

# json_data = """
# {
#   "squadName": "Super hero squad",
#   "homeTown": "Metro City",
#   "formed": 2016,
#   "secretBase": "Super tower",
#   "active": true
# }
# """

# data = json.loads(json_data)
# print(data["formed"])

page = 1
while page < 5:
    url = "https://ecshweb.pchome.com.tw/search/v4.3/all/results?q=quest3&page={page}&sort=rnk/dc"

    response = requests.get(url)
    data = response.json()

    for prod in data["Prods"]:
        print(prod["Name"], prod["Price"])

    page += 1
