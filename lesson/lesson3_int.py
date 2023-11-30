a = "123"
# print(int(a) + 3)


y = 12.123
y = 12.123
y = 12.123
y = 12.123
y = 12.123
# print(int(y))

x = False
# print(int(x))
# print(type(int(x)))


# Decimal 四捨五入
print(round(123.123456, 2))

# 取最大
print(max(3, 4, 1, 2, 77, 44, 3))
# 取最小
print(min(3, 4, 1, 2, 77, 44, 3))
# 取絕對值
print(abs(-99))
# 次方
print(pow(3, 4))


import math

# 12.21345
# 無條件進位
print(math.ceil(12.21234))
# 無條件捨去
print(math.floor(12.21234))

# 2位數後無條件進位
# 1221.234
print(math.ceil(12.21234 * 100) / 100)

print(math.floor(12.21234 * 100) / 100)


import random

print(random.randint(0, 5))
# 0 1 2 3 4 5

# start end step
print(random.randrange(0, 10, 2))
# 0 1 2 3 4 5 6 7 8 9
# 0 2 4 6 8
