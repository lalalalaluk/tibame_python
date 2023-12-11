import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Stock/index.html"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

div_elements = soup.find_all("div", class_="title")

for div_element in div_elements:
    a_element = div_element.find("a")
    if "公告" not in a_element.string and "閒聊" not in a_element.string:
        print(a_element.string)
