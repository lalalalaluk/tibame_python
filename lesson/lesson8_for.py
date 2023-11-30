# for 變數 in 序列:
#   做事情


fruits = ["apple", "banana", "lemon"]

for fruit in fruits:
    print("I like " + fruit)


numbers = [1, 2, 3, 4, 5]

# for nnn3 in numbers:
#     print(nnn3 * nnn3)

# for i in range(10):
#     print("apple")

string = "hello python"
# for s in string:
#     if s in ["a", "e", "i", "o", "u"]:
#         print("有母音", s)

# for i in range(10):
#     if i == 5:
#         continue

#     print(i)

# for i in range(10):
#     if i == 5:
#         break

#     print(i)

fruits = ["apple", "banana", "lemon"]

# index = 0
# for fruit in fruits:
#     if index != 1:
#         print(fruit)

#     index += 1

# for index, value in enumerate(fruits):
#     if index != 1:
#         print(value)

nums = ["1", "22", "333", "332"]

# for index, value in enumerate(nums):
#     nums[index] = int(value) # type: ignore

nums = list(map(int, nums))

print(nums)
print(type(nums[0]))
