from django.shortcuts import render
from django.http import HttpResponse
import random

def hello(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    return HttpResponse(' '.join(map(str,lucky_numbers)))


def bye(request):
    return HttpResponse('Goodbye My Friend') 

def review(request):
    return render(request, 'myapp/review.html') 

def index(request):
    lucky_numbers = random.sample(range(1, 46), 6)
    draw_no = 1078

    context = {
        'lucky_numbers': lucky_numbers,
        'draw_no': draw_no,
    }

    return render(request, 'myapp/index.html', context) 

# 1. URL(/bye/)요청
# 2. myapp.views에서 bye라는 함수를 호출해야함
# 3. 응답으로 'Goodbye My Friend'라고 내보내야 함