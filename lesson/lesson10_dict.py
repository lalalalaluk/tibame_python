#  {key: value, key: value}


my_dict = {"apple": 100, "banana": 200, "lemno": 300}


# print(my_dict["apple1"])
# print(my_dict.get("lemno111"))

# my_dict["apple"] = 300
# print(my_dict)

# my_list = [1,2,3]
# my_list[0] = 200

# my_dict["orange"] = 150
# print(my_dict)

# del my_dict["apple"]
# print(my_dict)

# my_dict.clear()
# my_dict = {}
# print(my_dict)


for index, value in enumerate(["apple", "banana", "lemon"]):
    print(index, value)

for key, value in my_dict.items():
    if value >= 200:
        print(key, value)

# print(my_dict.keys())
# print(my_dict.values())

# print(len(my_dict))

# print("apple" in my_dict)
