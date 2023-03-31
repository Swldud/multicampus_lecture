from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    reward = forms.IntegerField()
    content = forms.Textarea()

    class Meta:
        model = Question
        # fields = ('name', 'age', 'balance', )
        fields = '__all__'


