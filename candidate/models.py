from django.db import models
from django.contrib.auth.models import User

class CandidateAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profession_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
