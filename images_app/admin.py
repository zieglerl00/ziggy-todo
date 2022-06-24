from django.contrib import admin

# Register your models here.
from images_app.models import Card, Rarity, CardType, Image

admin.site.register(Card)
admin.site.register(Rarity)
admin.site.register(CardType)
admin.site.register(Image)
