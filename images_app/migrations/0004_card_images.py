# Generated by Django 4.0.3 on 2022-06-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images_app', '0003_alter_card_card_type_alter_card_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
