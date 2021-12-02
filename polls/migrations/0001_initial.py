# Generated by Django 2.2.10 on 2021-12-02 09:58

import django.contrib.postgres.fields
from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Дата старта')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Текст вопроса')),
                ('question_type', models.CharField(choices=[('TEXT RESPONSE', 'text response'), ('SINGLECHOICEANSWER', 'single choice answer'), ('MULTIPLECHOICEANSWER', 'multiple choice answer')], max_length=25, verbose_name='Тип вопроса')),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=polls.models.get_default_option, size=None)),
                ('answer_position', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=polls.models.get_default_position, size=None)),
                ('polls', models.ManyToManyField(related_name='to_polls', to='polls.Poll')),
            ],
        ),
    ]
