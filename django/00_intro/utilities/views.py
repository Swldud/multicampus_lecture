from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from bs4 import BeautifulSoup

def get_lotto(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers.sort()

    draw_no = 1234

    context = {
            'lucky_numbers': lucky_numbers,
            'draw_no': draw_no,
        }
    
    return render(request, 'utilities/get_lotto.html', context) 

def this_week(request):
    
    url = 'https://search.naver.com/search.naver?&query=%EB%A1%9C%EB%98%90'

    # 요청은 클라이언트 프로그램을 통해 URL로 보낸다.

    res = requests.get(url)

    data = BeautifulSoup(res.text, 'html.parser')


    real_numbers = []

    for tag in data.select('.ball'):
            real_numbers.append(tag.text)
    # print(real_number)

    real_numbers = list(map(int, real_numbers))
    bonus_number = real_numbers.pop()
    draw_no = 1234

    context = {
            'real_numbers' : real_numbers,
            'bonus_number' : bonus_number,
            'draw_no': draw_no,
        }

    return render(request, 'utilities/this_week.html', context) 

def check_lotto(request):
    
    lucky_numbers = random.sample(range(1, 46), 6)
    lucky_numbers = ' '.join(map(str,lucky_numbers))

    draw_no = 1234

    url = 'https://search.naver.com/search.naver?&query=%EB%A1%9C%EB%98%90'
    res = requests.get(url)
    data = BeautifulSoup(res.text, 'html.parser')

    real_numbers = []

    for tag in data.select('.ball'):
            real_numbers.append(tag.text)
    # print(real_number)

    real_numbers = list(map(int, real_numbers))
    bonus_number = real_numbers.pop()


    result = len(set(lucky_numbers) & set(real_numbers))
    rank = 0
     
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


    context = {
            'lucky_numbers': lucky_numbers,
            'draw_no': draw_no,
            'real_numbers' : real_numbers,
            'bonus_number' : bonus_number,
            'result' : result,
            'rank' : rank,

        }
    
    return render(request, 'utilities/check_lotto.html', context) 



