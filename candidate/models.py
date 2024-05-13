from django.db import models
from django.contrib.auth.models import User
from company.models import JobOpening

class CandidateAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profession_name = models.CharField(max_length=100)
    applied_jobs = models.ManyToManyField(JobOpening, related_name='applicants', blank=True)

    def __str__(self):
        return self.user.username
