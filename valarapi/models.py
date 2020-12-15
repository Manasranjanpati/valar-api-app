from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.conf import settings


class Quote(models.Model):

    class Meta:
        db_table = 'quote'
        verbose_name = 'Quotes Data'

    quote = models.TextField()
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()

    class Meta:
        ordering = ("-created",)
