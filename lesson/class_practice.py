# {'12345': 1000, '54123': 2000}


class BankAccount:
    def __init__(self, account_nubmer, balance):
        self.account_nubmer = account_nubmer
        self.balance = balance

    def deposit(self, ammount):
        self.balance += ammount

    def withdraw(self, price):
        if price > self.balance:
            print("餘額不足!")
        else:
            self.balance -= price

    def display_info(self):
        print(f"Account {self.account_nubmer} , Balance {self.balance} !")


class Bank:
    def __init__(self):
        self.account = {}

    def add_account(self, bank_account: BankAccount):
        if bank_account.account_nubmer in self.account:
            print("已經有此帳號 無法新增")
        else:
            self.account[bank_account.account_nubmer] = bank_account

    def list_account(self):
        for key, value in self.account.items():
            value.display_info()

    def delete_account(self, account_nubmer):
        del self.account[account_nubmer]

    def deposit_account(self, account_nubmer, price):
        self.account[account_nubmer].deposit(price)

    def withdraw_account(self, account_nubmer, price):
        self.account[account_nubmer].withdraw(price)


b = Bank()

while True:
    print("0. 顯示所有帳號")
    print("1. 新增帳號")
    print("2. 刪除帳號")
    print("3. 帳號存錢")
    print("4. 帳號領錢")

    action = input("請輸入動作:")

    if action == "0":
        b.list_account()
    elif action == "1":
        acount_number = input("請輸入帳號")
        balance = int(input("請輸入餘額"))
        a = BankAccount(acount_number, balance)
        b.add_account(a)
    elif action == "2":
        acount_number = input("請輸入帳號")
        b.delete_account(acount_number)
    elif action == "3":
        acount_number = input("請輸入帳號")
        balance = int(input("請輸入金額"))
        b.deposit_account(acount_number, balance)
    elif action == "4":
        acount_number = input("請輸入帳號")
        balance = int(input("請輸入金額"))
        b.withdraw_account(acount_number, balance)
