from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.
class First(models.Model):
    firstUrl = models.TextField()

class Keywords(models.Model):
    words = ArrayField(models.TextField())
    articles = ArrayField(models.TextField())
    matchedWords = ArrayField(ArrayField(models.TextField()))

class UserKeywords(models.Model):
    kw = models.OneToOneField(Keywords, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
