from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    amount = models.IntegerField()
    rarity = models.IntegerField()
    description = models.TextField()