from .models import Artiles, Answer
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Задать вопрос'
            }),
            "anons": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Теги'
            }),
            "full_text": Textarea(attrs={
                'class': "form"
            }),
            # "date": DateTimeInput(attrs={
            #     'class': 'form',
            #     'placeholder': 'Дата публикации'
            # })
        }
class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['full_text']

        widgets = {
            "full_text": Textarea(attrs={
                'class': 'form',
                'placeholder': 'Напишите свой ответ'
            })
        }