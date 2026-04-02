from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    is_slayed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slayed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
