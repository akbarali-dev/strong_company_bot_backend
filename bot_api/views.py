from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import BotUser, AnswerQuestions, Contact, File, Portfolio
from .serializer import UserSerializer, AnswerQuestionSerializer, ContactSerializer, FileSerializer, PortfolioSerializer


class UserDataAPIView(APIView):
    def get(self, request):
        user_data = BotUser.objects.get(bot_id=1474104201)
        user_data_serializer = UserSerializer(user_data)
        return Response(data=user_data_serializer.data)


class AnswerQuestionsAPIView(APIView):
    def get(self, request):
        user_data = BotUser.objects.get(bot_id=1474104201)
        questions = AnswerQuestions.objects.filter(user_id=user_data.bot_id)
        questions_serializer = AnswerQuestionSerializer(questions, many=True)
        return Response(data=questions_serializer.data)


class AnswerByQuestionsAPIView(APIView):
    def get(self, request, text):
        print(text)
        questions = AnswerQuestions.objects.filter(question__contains=text)
        questions_serializer = AnswerQuestionSerializer(questions.first())
        return Response(data=questions_serializer.data)


class ContactAPIView(APIView):
    def get(self, request):
        user_data = BotUser.objects.get(bot_id=1474104201)
        contact = Contact.objects.filter(user_id=user_data.bot_id)
        contact_serializer = ContactSerializer(contact, many=True)
        return Response(data=contact_serializer.data)


class FileAPIView(APIView):
    def get(self, request, pk):
        user_data = BotUser.objects.get(bot_id=1474104201)
        file = File.objects.filter(user_id=user_data.bot_id, category=pk)
        file_serializer = FileSerializer(file, many=True)
        return Response(data=file_serializer.data)


class PortfolioAllAPIView(APIView):
    def get(self, request):
        user_data = BotUser.objects.get(bot_id=1474104201)
        portfolio = Portfolio.objects.filter(user_id=user_data.bot_id)
        portfolio_serializer = PortfolioSerializer(portfolio, many=True)
        return Response(data=portfolio_serializer.data)


class PortfolioAPIView(APIView):
    def get(self, request, pk):
        user_data = BotUser.objects.get(bot_id=1474104201)
        portfolio = Portfolio.objects.get(id=pk)
        portfolio_serializer = PortfolioSerializer(portfolio)
        return Response(data=portfolio_serializer.data)
