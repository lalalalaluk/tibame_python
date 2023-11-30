fruits = {"apple": 100, "banana": 200, "lemno": 300}

while True:
    action = input("請輸入指令:\n")

    if action == "list":
        print(fruits)
    elif action == "query":
        fruit = input("你想要查什麼水果?\n")
        if fruit in fruits:
            print(f"水果{fruit}的價格為{fruits[fruit]}")
        else:
            print(f"沒有這個水果 {fruit}")
    elif action == "add":
        fruit = input("請輸入水果名稱")
        price = int(input("請輸入水果價格"))

        if fruit in fruits:
            print(f"無法新增 已經有此水果了")
        else:
            fruits[fruit] = price
            print(f"新增 {fruit} 成功")
    elif action == "update":
        fruit = input("請輸入水果名稱")
        if fruit in fruits:
            price = int(input("請輸入水果價格"))
            fruits[fruit] = price
            print(f"更新 {fruit} 成功")
        else:
            print(f"無法更新 沒有此水果")
    elif action == "delete":
        fruit = input("請輸入水果名稱")
        if fruit in fruits:
            del fruits[fruit]
            print(f"刪除 {fruit} 成功")
        else:
            print(f"無法刪除 沒有此水果")
    elif action == "quit":
        break
    else:
        print("沒有這個指令")
