from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import Notice

def board_def(request):

    return render(request, 'board_def.html')


def new(request):
    # 새로운 공지글을 작성하는 HTML(<form>)을 제공
    return render(request, 'board/new.html')

def create(request):
    notice = Notice()
    notice.title = request.POST['title']
    notice.rank = request.POST['rank']
    notice.content = request.POST['content']
    notice.save()

    return redirect (f'/board/{notice.pk}/')


def index (request):
    notices = Notice.objects.all()

    return render(request, 'board/index.html', {'notices': notices,} )

def detail(request, notice_pk):
    notice = Notice.objects.get(pk = notice_pk)
    return render(request, 'board/detail.html', {'notice': notice,} )


def delete(request, notice_pk):
    notice = Notice.objects.get(pk = notice_pk)
    notice.delete()
    return redirect('/board/')

def edit(request, notice_pk):
    #1. form action 
    notice = Notice.objects.get(pk = notice_pk)
    return render(request, 'board/edit.html', {'notice': notice,})


def update(request, notice_pk):
    notice = Notice.objects.get(pk = notice_pk)
    notice.title = request.POST['title']
    notice.rank = request.POST['rank']
    notice.content = request.POST['content']
    notice.save()

    return redirect(f'/board/{notice.pk}/')
