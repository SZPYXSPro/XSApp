from django.db import models

# Create your models here.

class Tags(model.Model):
    title=models.CharField(max_length=20)
