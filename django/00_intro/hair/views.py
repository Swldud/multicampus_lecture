from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def nice(request):
    # render의 첫번째 인자 = request로 고정
    # 두번째 인자 = 템플릿 인자 'str'
    return render(request, 'nice.html')


# /myapp/review/ 
# => review 뷰 함수 실행 
# => review.html 을 화면에 보여줌
# review.html 에는 오늘 배운 내용을 정리해서 HTML로 작성하세요