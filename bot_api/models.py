from django.db import models


class BotUser(models.Model):
    bot_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    educations = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100)
    site_link = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='contacts')


class File(models.Model):
    CHOICES = (
        ('P', 'Portfolio'),
        ('S', 'Certificate'),
        ('R', 'Resume'),
    )
    file_link = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=CHOICES)
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='files')


class AnswerQuestions(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='answers')


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, related_name='portfolios')


class AnswerQuestionsNima(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
