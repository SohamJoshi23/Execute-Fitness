# models.py
from django.db import models

class Membership(models.Model):
    FULL_NAME_MAX_LENGTH = 100
    PHONE_NUMBER_MAX_LENGTH = 15
    EMAIL_MAX_LENGTH = 100
    MEMBERSHIP_CHOICES = [
        ('Basic', 'Basic'),
        ('Ultimate', 'Ultimate'),
        ('Premium', 'Premium'),
    ]

    full_name = models.CharField(max_length=50,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES,null=True)

    def __str__(self):
        return f"{self.full_name}"
