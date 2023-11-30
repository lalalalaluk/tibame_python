a = input().split()
weekday = a[0]

if weekday == "星期一" or weekday == "星期二" or weekday == "星期三" or weekday == "星期四":
    print(int(a[1]) * int(a[2]))
else:
    print("不開市")
