from django import forms
from .models import Student



# 1. 사용자 입력의 검증 (유효성 검증 validation)
# 2. views에서 입력 <-> 필드에 직접 매칭 귀찮
# 3. HTML에서 input 태그 생성 귀찮


class StudentForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    balance = forms.IntegerField()
    major = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=20)
    mbti = forms.CharField(max_length=4)
    address = forms.CharField(max_length=100)

    class Meta:
        model = Student
        # fields = ('name', 'age', 'balance', )
        fields = '__all__'
