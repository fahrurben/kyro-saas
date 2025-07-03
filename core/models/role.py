from django.db import models

SUPER_ADMIN = 'SA'
COMPANY_ADMIN = 'CA'
BLOG_ADMIN = 'BA'

class Role(models.TextChoices):
    SUPER_ADMIN = 'SA', 'Super Admin'
    COMPANY_ADMIN = 'CA', 'Company Admin'
    BLOG_ADMIN = 'BA', 'Blog Admin'
