from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm


# def new(request):
#    form = StudentForm()

#    return render(request, 'blog/new.html', {
#        'form': form, })

#def create(request):
    # form 에 사용자 입력 데이터 붙임
#    form = StudentForm(request.POST)
    
    # data가 유효하다면,
#    if form.is_valid():
#        form.save()
#        return redirect('/blog/new/')
    # data가 유효하지 않다면
#    else:
#        return render(request, 'blog/new.html', {
#            'form': form       })
    


# 위의 new와 create를 합쳐서 만든 create

def create(request):
    if request.method == 'GET':
        form = StudentForm()
        
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('detail', student.pk)
        
    return render(request, 'blog/new.html', {
        'form': form
    })


def index(request):
    students = Student.objects.order_by('-balance')

    return render(request, 'blog/index.html', {'students': students})


def detail(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    return render(request, 'blog/detail.html', {
        'student': student,
    })


# def edit(request, student_pk):
#     student = Student.objects.get(pk=student_pk)
#     form = StudentForm(instance=student)

#     return render(request, 'blog/edit.html', {
#         'student': student,
#         'form': form,
#     })


# def update(request, student_pk):
#     student = Student.objects.get(pk=student_pk)
#     form = StudentForm(request.POST, instance=student)
    
#     # data가 유효하다면,
#     if form.is_valid():
#         student = form.save()
#         return redirect(f'/blog/{student.pk}/')
#     # data가 유효하지 않다면
#     else:
#         return render(request, 'blog/edit.html', {
#             'form': form,
#         })


def update(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    if request.method == 'GET':
        form = StudentForm(instance=student)
        
    elif request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            # return redirect(f'/blog/{student.pk}/')
            return redirect('detail', student.pk)

    return render(request, 'blog/edit.html', {
        'form': form,
    })


def delete(request, student_pk):
    student = Student.objects.get(pk = student_pk)
    student.delete
    return redirect('index')