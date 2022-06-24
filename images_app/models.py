from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Rarity(models.Model):
    rarity = models.CharField(max_length=255)
    verbose_name = "Rarity"

    def __str__(self):
        return self.rarity


class CardType(models.Model):
    card_type = models.CharField(max_length=255)
    verbose_name = "CardType"

    def __str__(self):
        return self.card_type


class Card(models.Model):
    card = models.CharField(max_length=255)
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    card_type = models.ForeignKey(CardType, on_delete=models.CASCADE)
    verbose_name = "Card"

    def __str__(self):
        return self.card


class Image(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to='static/photos')