from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'myapp/hello.html', context)

def ping(request):

    return render(request, 'myapp/ping.html')


def pong(request):
    # POST 방식
    # 1. <form method="POST">
    # 2. <form> > {% csrf_token %}
    # 3. view => request.POST
    context = {
        'name': request.POST['user_name'],
        'age': request.POST['age'],
        'MBTI': request.POST['MBTI'],
    }
    return render(request, 'myapp/pong.html', context)

def lotto_in(request):

    return render(request, 'myapp/lotto_in.html')

def lotto_out(request):

    draw_no = request.GET["no"]

    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8".format(draw_no)
    # url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={draw_no}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"

    res = requests.get(url)

    data = BeautifulSoup(res.text, 'html.parser')


    real_numbers = []

    for tag in data.select('.ball'):
            real_numbers.append(tag.text)
    # print(real_number)

    real_numbers = list(map(int, real_numbers))
    bonus_number = real_numbers.pop()

    lucky_numbers = request.GET["lucky_numbers"]
    lucky_numbers = lucky_numbers.split()
    lucky_numbers = list(map(int, lucky_numbers))

    result = len((set(lucky_numbers) & set(real_numbers)))
    # print(result)
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
    
    'draw_no' : request.GET["no"],
    'lucky_numbers' : request.GET["lucky_numbers"],
    'real_numbers' : real_numbers,
    'bonus_number' : bonus_number,
    'result' : result,
    'rank' : rank,
        
    }
    
    return render(request, 'myapp/lotto_out.html', context)

