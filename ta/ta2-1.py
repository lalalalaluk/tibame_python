x, y = input().split()
x = int(x)
y = int(y)

# x = 3
# 1 2 3
#
# y =4
# 1 2 3 4

for i in range(x):
    print(x)
    for j in range(y):
        print(f"{i}{j}")
        print(f"{i+1}x{j+1}={(i+1)*(j+1)}")

i = 1
while i <= x:
    j = 1
    print(j)
    while j <= y:
        print(f"{i}{j}")
        print(f"{i}x{j}={i*j}")
        j += 1
    i += 1
