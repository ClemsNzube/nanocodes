# faq/views.py
from rest_framework import generics, permissions
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]  

    def perform_create(self, serializer):
        serializer.save()

class AnswerListCreateView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]  

    def perform_create(self, serializer):
        serializer.save()

class AnswerListByQuestionView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]  

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return Answer.objects.filter(question_id=question_id)
