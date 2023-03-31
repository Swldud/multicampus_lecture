import crawling
import random
import requests
from bs4 import BeautifulSoup

print(crawling.get_real_data)

url = 'https://search.naver.com/search.naver?&query=%EB%A1%9C%EB%98%90'

# 요청은 클라이언트 프로그램을 통해 URL로 보낸다.

res = requests.get(url)

data = BeautifulSoup(res.text, 'html.parser')


real_number = []

for tag in data.select('.ball'):
        real_number.append(tag.text)
# print(real_number)

real_number = list(map(int, real_number))
bonus_number = real_number.pop()


cnt = {
    'all': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
}

while 1:
    cnt['all'] += 1
    lucky_numbers = random.sample(range(1, 46), 6)
    match_count = len(set(lucky_numbers) & set(real_number))

    if match_count == 6:
        print('1등!', cnt)
        break
    elif match_count == 5 and bonus_number in lucky_numbers:
        cnt['2'] += 1
        # print('2등')
    elif match_count == 5:
        cnt['3'] += 1
    elif match_count == 4:
        cnt['4'] += 1
        # print('4등')
    elif match_count == 3:
        cnt['5'] += 1
        # print('5등')