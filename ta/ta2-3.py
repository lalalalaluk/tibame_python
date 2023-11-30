n = int(input())

array = []

for j in range(n):
    if j == 0:
        array.append("0")
    elif j == 1:
        array.append("1")
    else:
        first = 0
        second = 1

        #  0 1 1 2 3 5 8 13 21
        # n = 3 -> 1

        # 目標 跑n-2次迴圈

        for i in range(1, j):
            # temp = first
            # first = second
            # second = temp + second

            first, second = second, first + second

        array.append(str(second))

    # index = 2
    # while index < n:
    #     temp = first
    #     first = second
    #     second = temp + second

    #     index += 1

    # print(second)


print(" ".join(array))
print(array[10])
