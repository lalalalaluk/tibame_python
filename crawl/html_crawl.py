from bs4 import BeautifulSoup

html_src = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My website</title>

    <style>
        .btn {
            color: brown;
            padding: 30px;
        }
    </style>

</head>

<body>
    <!-- Header1 -->
    <h1>Header1</h1>
    <h2>Header2</h2>
    <h3>Header3</h3>
    <h4>Header4</h4>
    <h5>Header5</h5>

    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Necessitatibus culpa, magnam laudantium minus dolor
        mollitia, doloribus id quia asperiores quae iusto reiciendis fuga. Ipsam dolor perspiciatis, soluta voluptatibus
        fugiat corrupti?</p>

    <button id="btn1" class="btn">Click me</button>
    <br>
    <button id="btn2" class="btn">Click me 2</button>
    <br>

    <div style="color: red;">
        <p>123</p>
        <p>456</p>
        <p>789</p>
    </div>

    <input type="text">
    <input type="password">

    <ol>
        <li>apple</li>
        <li id="second">banana</li>
        <li>lemon</li>
    </ol>

    <ul>
        <li>apple</li>
        <li >banana</li>
        <li class="c3">lemon</li>
    </ul>

    <a href="https://www.google.com.tw/">this is hyper link</a>

</body>

</html>
"""

soup = BeautifulSoup(html_src, "html.parser")

# print(soup.button)
# print(soup.button.string)

# for button in soup.find_all("button"):
#     print(button)
#     print(button.string)

# print(soup.find(id="btn1").string)
# print(soup.find(class_="btn").string)

# print(soup.find("li", id="second"))
print(soup.find("li", class_="c3"))
