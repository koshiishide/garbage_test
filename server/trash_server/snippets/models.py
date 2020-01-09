from django.db import models


class Snippet(models.Model):#ゴミ箱の情報
    created      = models.DateTimeField(auto_now_add=True)
    name         = models.CharField(max_length=100,blank=True, default='')
    people       = models.CharField(max_length=100, blank=True, default='')
    amount_trash = models.TextField()
    class Meta:
        ordering = ('created',)

class MapField(models.Model):
    #仮想マップ
    client = models.CharField(default = 'Unknown', max_length=50)
    x      = models.IntegerField(default = 0)
    y      = models.IntegerField(default = 0)

class AllNode(models.Model):#初期化先
    #現在情報
    client = models.CharField(default = 'Unknown', max_length=50)
    x      = models.CharField(default = 0,max_length = 100)
    y      = models.CharField(default = 0,max_length = 100)

class Client_Queue(models.Model):
    client = models.CharField(default = 'Unknown', max_length=50)

class Culc_bit(models.Model):
    client = models.IntegerField(default = 0)
#過去情報
"""
class OldData(models.Model)
"""
