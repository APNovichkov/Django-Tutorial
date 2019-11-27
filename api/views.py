from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from polls.models import Question, Choice
from api.serializers import QuestionSerializer
from api.serializers import ChoiceSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView


class QuestionList(ListCreateAPIView):
    queryset = Question.objects.all()[:20]
    serializer_class = QuestionSerializer

class QuestionDetail(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
