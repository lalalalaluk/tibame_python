# {'12345': 1000, '54123': 2000}


bank_account1 = {"account_nubmer": "1234", "balance": 1000}

# 存款
# bank_account1["balance"] += 500

# # 領錢
# if bank_account1["balance"] > 700 + 10:
#     bank_account1["balance"] -= 700
# else:
#     print("餘額不足!")


bank_account2 = {"account_nubmer": "1235", "balance": 2000}
# bank_account2["balance"] += 500
# bank_account2["balance"] += 400

# # 領錢
# if bank_account2["balance"] > 600:
#     bank_account2["balance"] -= 600
# else:
#     print("餘額不足")


bank1 = {"1234": bank_account1, "1235": bank_account2}

while True:
    account = input("請輸入帳號")
    money = int(input("請輸入金額"))

    bank1[account]["balance"] += money

    print(bank1[account])
