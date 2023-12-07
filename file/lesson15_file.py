# file = open("file.txt", "r")

# lines = file.readlines()

# for line in lines:
#     print(line.strip())


# file.close()

# # 不用close
# with open("file.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()

#     for line in lines:
#         print(line.strip())


# r read w write a apend
# with open("file.txt", "a", encoding="utf-8") as file:
#     file.write("hello world\n")

with open("hello.py", "w", encoding="utf-8") as file:
    content = 'print("hello python")'
    file.write(content)
