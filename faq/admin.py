# faq/admin.py
from django.contrib import admin
from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at',)
    search_fields = ('text',)
    list_filter = ('created_at',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'created_at',)
    search_fields = ('question__text', 'text',)
    list_filter = ('created_at',)
