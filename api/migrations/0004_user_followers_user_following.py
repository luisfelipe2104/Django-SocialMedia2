# Generated by Django 4.0.4 on 2022-09-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]