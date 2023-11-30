# 1~100
# 33
# 77  1~77
# 22  22~77
# 55  22~55

import random

ans = random.randint(1, 100)

min_num = 1
max_num = 100

while True:
    guess = int(input(f"請從{min_num}到{max_num}猜一個數字"))
    if guess == ans:
        print("賓果!你猜中了")
        break
    else:
        if guess < ans:
            min_num = guess
        elif guess > ans:
            max_num = guess
