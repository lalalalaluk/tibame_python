# while 條件:
#   做事情

index = 1
sum = 0


while index <= 10:
    sum += index
    index += 1

print(sum)

# continue break
# index = 1
# sum = 0

while index <= 10:
    if index == 5:
        index += 1
        continue

    sum += index
    index += 1

# print(sum)

# index = 1
# sum = 0

while index <= 10:
    if index == 5:
        index += 1
        break

    print(index)
    sum += index
    index += 1

# print(sum)

while True:
    a = input()
    print(a)
