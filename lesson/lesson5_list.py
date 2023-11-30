# a = ["apple", "banana", 3, True, 3.14159]

# print(a)
# print(len(a))

# print(a[0])
# print(a[3])
# print(a[-1])

# print(a[1:4])
# print(a[:4])
# print(a[1:])
# print(a[-3:])
# print(a[:-3])
# print(a[::2])
# print(a[4:1:-1])
# print(a[::-2])

# 新增
# a.append("lemon")
# a.append("watermelon")
# print(a)

# a.insert(1, 6.666)
# print(a)

# a = ["apple", "banana", 3, True, 3.14159]
# b = ["bbb", "ccc"]

# print(a + b)
# print(b * 10)

# 刪除元素 del remove
# del a[1:3]
# print(a)

# a.remove(True)
# print(a)

# b = a.pop()
# print(b)
# print(a)

# a.clear()
# print(a)

# 修改
# a[0] = "grape"
# a[2] = 33
# print(a)

# 排序 從小到大 reverse = 從大到小
# a = [1, 2, 33, 44, 5, 77, 22, 12]
# a.sort(reverse=True)
# print(a)

# b = sorted(a, reverse=True)
# print(b)

# 反轉
# a.reverse()
# print(a)
# print(a[::-1])


# 深複製 淺複製

# a = 5
# b = a
# a = 6

# print(b)

# a = [1, 2, 3]
# b = a
# a[0] = 5

# print(b)

# a = [1, 2, 3]
# b = a.copy()
# a[0] = 5
# print(b)

# b = a[:]
# a[0] = 5
# print(b)

# b = list(a)
# a[0] = 5
# print(b)

# deeepcopy
# a = [0, 1, 2, 3, 4, 5, [33, 44, 55, ["ee", "cc"]]]

# b = a[:]
# c = a.copy()
# d = list(a)

# import copy

# e = copy.deepcopy(a)

# a[-1][0] = 66

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


# a = [1, 2, 3, 44, 5, 2, 2]
# print(2 in a)

# print(max(a))
# print(min(a))

# print(a.count(1111))

c = ["hello", "world", "python", "3"]
result = "/".join(c)
print(result)
