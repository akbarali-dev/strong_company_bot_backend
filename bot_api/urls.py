from django.urls import path
from .views import UserDataAPIView, AnswerQuestionsAPIView, ContactAPIView, FileAPIView, PortfolioAPIView, PortfolioAllAPIView, AnswerByQuestionsAPIView
urlpatterns = [
    path('data/', UserDataAPIView.as_view()),
    path('qa/', AnswerQuestionsAPIView.as_view()),
    path('qa/<str:text>/', AnswerByQuestionsAPIView.as_view()),
    path('contact/', ContactAPIView.as_view()),
    path('portfolio/', PortfolioAllAPIView.as_view()),
    path('portfolio/<int:pk>/', PortfolioAPIView.as_view()),
    path('file/<str:pk>/', FileAPIView.as_view()),
]
