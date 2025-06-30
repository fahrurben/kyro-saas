from django.db import models

from .custom_user import CustomUser
from .company import Company

class Role(models.TextChoices):
    SUPER_ADMIN = 'SA', 'Super Admin'
    COMPANY_ADMIN = 'CA', 'Company Admin'
    BLOG_ADMIN = 'BA', 'Blog Admin'

class UserRole(models.Model):
    user = models.ForeignKey(CustomUser, related_name='roles', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=Role, default=Role.COMPANY_ADMIN)

