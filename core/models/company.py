from django.db import models

from .company_manager import CompanyManager

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    objects = CompanyManager()
    default_objects = models.Manager()
