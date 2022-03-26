from django.db import models


class Comment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
