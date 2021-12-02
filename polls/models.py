from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата старта')
    end_date = models.DateField(verbose_name='Дата окончания')
    description = models.TextField(verbose_name='Описание')
        
    def __str__(self):
        return f'{self.name}'
    
    
class Question(models.Model):
    QUESTIONSTYPES = (
            ('TEXT RESPONSE', 'text response'),
            ('SINGLECHOICEANSWER', 'single choice answer'), 
            ('MULTIPLECHOICEANSWER', 'multiple choice answer'),
        )
    question_text = models.TextField(verbose_name='Текст вопроса')
    question_type = models.CharField(max_length=25, choices=QUESTIONSTYPES, verbose_name='Тип вопроса')
    polls = models.ManyToManyField(Poll, related_name='to_polls')
    
    def __str__(self):
        return f'{self.question_text}'
    

