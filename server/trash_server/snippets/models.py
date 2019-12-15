from django.db import models


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100,blank=True, default='')
    people = models.CharField(max_length=100, blank=True, default='')
    amount_trash = models.TextField()

    class Meta:
        ordering = ('created',)


class MapField(models.Model):
    client = models.CharField(default = 'Unknown', max_length=50)
    x      = models.IntegerField(default = 0)
    y      = models.IntegerField(default = 0)

