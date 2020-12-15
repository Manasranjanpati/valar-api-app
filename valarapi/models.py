from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.text} by {self.author} (submitted by {self.user})"

    def get_absolute_url(self):
        return reverse('quote_detail', args=f"{self.id}")

    class Meta:
        ordering = ("-created",)
