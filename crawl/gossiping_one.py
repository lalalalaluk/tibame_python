import requests


header = {"cookie": "over18=1"}

response = requests.get("https://www.ptt.cc/bbs/Gossiping/index.html", headers=header)
print(response.text)
