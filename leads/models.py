from django.db import models
from django.conf import settings

class Lead(models.Model):

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Interested', 'Interested'),
        ('Converted', 'Converted'),
        ('Lost', 'Lost'),
    ]

    SOURCE_CHOICES = [
        ('Website', 'Website'),
        ('Social Media', 'Social Media'),
        ('Referral', 'Referral'),
        ('Advertisement', 'Advertisement'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    company = models.CharField(max_length=200, blank=True, null=True)

    source = models.CharField(
        max_length=50,
        choices=SOURCE_CHOICES
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )

    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='leads'
    )

    def __str__(self):
        return self.name