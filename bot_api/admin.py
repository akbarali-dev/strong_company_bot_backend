from django.contrib import admin

from .models import BotUser, File, Contact, AnswerQuestions, Portfolio


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'job_title')
    search_fields = ('full_name', 'age', 'job_title')
    list_per_page = 20


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file_link', 'user')
    list_per_page = 20


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'link')
    search_fields = ('user',)


@admin.register(AnswerQuestions)
class AnswerQuestionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer')
    search_fields = ('question', 'user')
    list_per_page = 20


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description')
    search_fields = ('user', 'title', 'description')
    list_per_page = 20
