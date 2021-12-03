from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Poll(models.Model): # Модель опросов
    name = models.CharField(max_length=256, verbose_name='Название')
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата старта')
    end_date = models.DateField(verbose_name='Дата окончания')
    description = models.TextField(verbose_name='Описание')
            
    def __str__(self):
        return f'{self.name}'
    

class Question(models.Model): # Модель вопросов опроса
    QUESTIONSTYPES = (
            ('TEXT RESPONSE', 'text response'),
            ('SINGLECHOICEANSWER', 'single choice answer'), 
            ('MULTIPLECHOICEANSWER', 'multiple choice answer'),
        )
    question_text = models.TextField(verbose_name='Текст вопроса')
    question_type = models.CharField(max_length=25, choices=QUESTIONSTYPES, verbose_name='Тип вопроса')
    polls = models.ManyToManyField(Poll, blank=True, through='PollQuestion')
    options = ArrayField(models.CharField(max_length=256), blank=True)
    answer_position = ArrayField(models.IntegerField())
    
    def __str__(self):
        return f'{self.question_text}'
    
    
class PollQuestion(models.Model): # Модель для связи МкМ меджу Опросами и Вопросами
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Answer(models.Model): # Модель ответов к вопросам
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.text}'
    

class Select(models.Model): # Модель выбора ответов пользователем на вопросы
    question = models.ForeignKey(Question, related_name='selected', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_select', on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)
    selected_answer = ArrayField(models.IntegerField())
        
    def __str__(self) -> str:
        return f'{self.question} {self.user} {self.answer}'
    
    def save(self, *args, **kwargs):
        if self.question.answer_position == self.selected_answer:
            self.answer = True
        else:
            self.answer = False
        super().save(*args, **kwargs)
        

