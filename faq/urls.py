from django.urls import path
from .views import QuestionListCreateView, AnswerListCreateView, AnswerListByQuestionView

urlpatterns = [
    path('questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('answers/', AnswerListCreateView.as_view(), name='answer-list-create'),
    path('questions/<int:question_id>/answers/', AnswerListByQuestionView.as_view(), name='answer-list-by-question'),
]
