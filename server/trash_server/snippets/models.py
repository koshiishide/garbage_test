from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    people = models.CharField(max_length=100, blank=True, default='')
    amount_trash = models.TextField()

    class Meta:
        ordering = ('created',)
