import requests
from bs4 import BeautifulSoup

def get_real_data():
      
    url = 'https://search.naver.com/search.naver?&query=%EB%A1%9C%EB%98%90'

    # 요청은 클라이언트 프로그램을 통해 URL로 보낸다.

    res = requests.get(url)

    data = BeautifulSoup(res.text, 'html.parser')

    # print(data.select('.ball'))
    real_number = []

    for tag in data.select('.ball'):
            real_number.append(tag.text)
    # print(real_number)

    real_number = list(map(int, real_number))
    bonus_number = real_number.pop()

    #print(real_number, bonus_number)

    return real_number, bonus_number

    # for tag in data.select('.ball'):
        #print(tag.text)

# print(get_real_data())

# list(map(lambda tag: int(tag.text), data.select('.ball))) 은 위의 4줄로 만든 추출식과 같다.


