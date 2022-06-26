from django.db import models
from app_user.models import User


class Message(models.Model):
    """
    message model
    """
    text = models.CharField(max_length=256)
    sender = models.ForeignKey(User, models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, models.CASCADE, related_name='recipient')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """to string"""
        return f"{self.sender} to {self.recipient}"
