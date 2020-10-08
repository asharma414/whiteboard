from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
