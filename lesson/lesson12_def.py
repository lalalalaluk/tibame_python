# def name():
#     print("hello name")
#     print("hello name111")
#     print("hello name2")
#     print("hello name3")
#     print("hello name4")


# for i in range(10):
#     if i == 3:
#         name()
#     if i == 5:
#         name()
#     if i == 9:
#         name()


def greet(name, age):
    return f"Hello, {name} , nice to meet you, your age is {age}"


print(greet(age=10, name="Jack"))
# greet("Luke", 15)
# greet("John", 25)

# print(s + " print by return")

# def cal_area(length: int, width:int =5):
#     return length * width


# print(cal_area(5, 10) + cal_area(3, 6) + cal_area(3))


def cal_average(*numbers):
    return sum(numbers) / len(numbers)


print(cal_average(1, 2, 3, 4, 5))
