a = input()

if "+" in a:
    numbers = a.split("+")
    print(int(numbers[0]) + int(numbers[1]))
elif "-" in a:
    numbers = a.split("-")
    print(int(numbers[0]) - int(numbers[1]))
elif "*" in a:
    numbers = a.split("*")
    print(int(numbers[0]) * int(numbers[1]))
elif "/" in a:
    numbers = a.split("/")
    print(int(int(numbers[0]) / int(numbers[1])))
