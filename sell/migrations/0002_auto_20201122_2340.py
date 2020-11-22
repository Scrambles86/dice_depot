# Generated by Django 3.0.8 on 2020-11-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_description',
            field=models.TextField(blank=True, help_text="Please provide a quick description of your game's quality", max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='model_pic',
            field=models.ImageField(default='', upload_to='user_game_images/'),
        ),
    ]
