from django.forms import ModelForm, Form
import django.forms as forms
from django.contrib.auth import get_user_model

from images_app.models import Card

User = get_user_model()


class EditAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class AddCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["card", "rarity", "card_type"]

