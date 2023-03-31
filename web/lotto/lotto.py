import random

lucky_numbers = random.sample(range(1,46),6)
real_numbers = [11, 23, 25, 30, 32, 40]
bonus_number = 42

result = len(set(lucky_numbers) & set(real_numbers))

if result == 6:
    rank = 1

elif result == 5:
    if bonus_number in lucky_numbers:
        rank = 2
    else:
        rank = 3

elif result == 4:
    rank = 4

elif result ==3:
    rank = 5    

else:
    rank = 0


print(f'{lucky_numbers} {rank}등 입니다.')
