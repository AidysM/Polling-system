from django.contrib import admin

from .models import Poll, Question, PollQuestion


class PollQuestionInline(admin.TabularInline):
    model = PollQuestion
    extra = 1

class PollQuestionAdmin(admin.ModelAdmin):
    inlines = (PollQuestionInline,)
    

admin.site.register(Question)

admin.site.register(Poll, PollQuestionAdmin)
