import requests
from bs4 import BeautifulSoup


def get_stock(url):
    header = {"cookie": "over18=1"}

    response = requests.get(url, headers=header)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    div_elements = soup.find_all("div", class_="title")

    for div_element in div_elements:
        a_element = div_element.find("a")
        if a_element and "公告" not in a_element.string and "閒聊" not in a_element.string:
            print(a_element.string)

    next_link = soup.find("a", string="‹ 上頁")

    return "https://www.ptt.cc" + next_link.get("href")


url = "https://www.ptt.cc/bbs/Gossiping/index.html"

next_page = get_stock(url)
page = 0

while page < 10:
    next_page = get_stock(next_page)
    page += 1
