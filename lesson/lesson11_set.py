# set 元素不重複

my_set = {1, 2, 3, 4, 5, 2, 3, 2, 3}

# print(type(my_set))
# print(my_set)

my_set.add(7)
my_set.add(8)
# print(my_set)

# my_set.remove(5)
my_set.discard(5)
# print(my_set)


# my_list = [1, 2, 3, 4, 5, 2, 3, 2, 3]
# my_set = set(my_list)
# print(my_set)

# for s in my_set:
#     print(s)

print(3 in my_set)

# 集合運算
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}


# 取交集
print("交集", set1.intersection(set2))

# 取聯集
print("聯集", set1.union(set2))

# 差集
print("差集", set1.difference(set2))

# 對稱差集
print("對稱差及", set1.symmetric_difference(set2))
