# Generated by Django 4.0.4 on 2022-04-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_answer_options_rename_question_answer_que_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата публикации'),
        ),
    ]
