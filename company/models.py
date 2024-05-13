from django.db import models
from django.contrib.auth.models import User

class CompanyAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    bio = models.TextField()

class JobOpening(models.Model):
    jobid = models.AutoField(primary_key=True)
    company = models.ForeignKey(CompanyAuth, on_delete=models.CASCADE, null=True)
    job_title = models.CharField(max_length=100)
    experience_needed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_description = models.TextField()
    last_date_for_application = models.DateField()

    def company_name(self):
        if self.company:
            return self.company.company_name
        else:
            return None

   