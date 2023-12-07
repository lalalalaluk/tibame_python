# NameError
# x = 10
# print(y)

# import math

# print(mathx.sqrt(16))

# def greet(name):
#     print(name)

# greeta("john")

# IndexError
# my_list = [1, 23, 4]
# my_list[5]

# my_tuple = (1, 2323, 43)
# my_tuple[5]

# TypeError
# print("hello" + 5)
# l = [12, 34, 5, "a"]
# print(sum(l))

# SyntaxError
# if 5 > 2:
#     print("bigger")

# l = [12,23,4,5
# print(l)

# ValueError
# a = int("123")
# a = int("abc")

# ZeroDivisionError
# print(10 / 0)

# try:
#     i = int(input())
#     print(10 / i)
# except ZeroDivisionError as e:
#     print("不能輸入0 因為會有無限大的錯誤")

# try:
#     i = int(input())
#     print(10 / i)
# except Exception as e:
#     print("錯誤:", str(e))


def create_password(pwd):
    try:
        if len(pwd) < 8:
            # print('密碼不小於8')
            raise ValueError("密碼必須大於8位數")
        elif len(pwd) > 16:
            raise ValueError("密碼必須小於16位數")
        elif "$" in pwd:
            raise Exception("特殊符號錯誤")
    except ValueError as e:
        print("長度問題", e)
    except Exception as e:
        print(e)


pwd = input("請輸入密碼\n")
create_password(pwd)
