from django.db import models


class Spot(models.Model):
    # 名前
    name = models.CharField(max_length=50)
    # カテゴリー
    category = models.CharField(max_length=5, blank=True)
    # ジャンル
    genre = models.CharField(max_length=50, blank=True)
    # 都道府県
    address_prefecture = models.CharField(max_length=10, blank=True)
    # 市区町村
    address_city = models.CharField(max_length=10, blank=True)
    # 丁目番地等
    address_street = models.CharField(max_length=100, blank=True)
    # 緯度
    latitude = models.CharField(max_length=50, blank=True)
    # 経度
    longitude = models.CharField(max_length=50, blank=True)
    # 作成日
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
