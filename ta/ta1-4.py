numbers = input().split(",")

player_list = numbers[0].split()
com_list = numbers[1].split()

count = 0
if player_list[0] in com_list:
    count += 1
if player_list[1] in com_list:
    count += 1
if player_list[2] in com_list:
    count += 1
if player_list[3] in com_list:
    count += 1
if player_list[4] in com_list:
    count += 1

if count < 3:
    print("0")
elif count == 3:
    print(100)
elif count == 4:
    print(1000)
elif count == 5:
    print(10000)
