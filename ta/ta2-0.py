n = int(input())
sum = 0

# 5
# 1 2 3 4 5
# index = 1
# while index <= n:
#     sum += index
#     index += 1

for i in range(n):
    sum = sum + (i + 1)

print(sum)
