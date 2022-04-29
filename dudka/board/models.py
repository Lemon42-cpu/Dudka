from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название', max_length=70)
    anons = models.CharField('Тема', max_length=250)
    full_text = models.TextField('Текст вопроса')
    date = models.DateTimeField('Дата публикации', auto_now=True)
    rang = models.IntegerField('Рейтинг', blank=True, null=True)
    comp = models.BooleanField('Решенный', default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/board/{self.id}'

    class Meta:
        db_table = 'que'
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'



class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    full_text = models.TextField('Текст вопроса')
    date = models.DateTimeField('Дата публикации', auto_now=True)
    rang = models.IntegerField('Рейтинг', blank=True, null=True)
    comp = models.BooleanField('Решение', default=False)
    que = models.ForeignKey(Artiles, verbose_name='Вопрос', on_delete=models.CASCADE)
    def __str__(self):
        return self.full_text

    def get_absolute_url(self):
        return f'/board/{self.id}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'