from django.db import models
from django.contrib.auth import get_user_model 

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_lenght = 200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model())
    create_date = models.DateTimeField()
    published_date = models.DateTimeField()

