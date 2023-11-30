a = "This is"
b = "banana"

# print(a)
# print(b)
# print(type(a))

# c = 123

# print(a + str(c))
# print(a + " " + str(c) * 10)


# s = "Hello, world"

# [start, end, step]

# print(s[-2])
# print(s[111])

# print("orgin", s)
# print("s[0:5]", s[0:5])
# print("s[1:5]", s[1:5])
# print("s[:5]", s[:5])
# print("s[5:]", s[5:])
# print("s[-5:]", s[-5:])
# print("s[1:-1]", s[1:-1])
# print("s[1:-1:2]", s[1:-1:2])
# print("s[:1:-1]", s[:1:-1])
# print("s[::-1]", s[::-1])

# s = "2022/04/03"

# print(s[])
# print(s[])
# print(s[])


name = "john"
age = 18

# print("My name is " + name + " and I am " + str(age) + " years old")

# # f-string
# print(f"My name is {name} and I am {age} years old")
# # format
# print("My name is {} and I am {} years old".format(name, age))

# 格式化
num = 3.14159
# print(num)

# print(f"{num:.3f} is 2 digit")
# print("{:.3f} is 2 digit".format(num))

# # 長度
# s = "hello python"
# print(len(s))

# # 移除頭尾的空白
# s = "   hello python   "
# print(s.strip())

# # 分割字串
# s = "apple-banaba-lemon"
# print(s.split("-"))

# # 取代
# s = "I like apple"
# print(s.replace("apple", "banana"))

# 轉義

s = "hello \n world \n python"
# print(s)
print(s.splitlines())

s = "I'm \" ' \" joho"
print(s)

# raw string
s = r"hello \n world \n python"
print(s)

s = """ this is 
multiple
line
line
line
"""
print(s)

s = (
    "this is tooooooooooooooooooo looooooongggggggggg"
    "ggggggggggg aaaaaaaaaaaaaaaaaaa"
    "ggggggggggg vvvvvvvvvvvvvv"
    "ggggggggggg cccccccccccccccccccccc"
)

print(s)
