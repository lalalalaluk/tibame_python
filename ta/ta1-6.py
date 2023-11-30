year = int(input())

if year % 4 != 0:
    print("False")
elif year % 4 == 0 and year % 100 != 0:
    print("True")
elif year % 100 == 0 and year % 400 != 0:
    print("False")
elif year % 400 == 0:
    print("True")
