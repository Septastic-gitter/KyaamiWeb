# Generated by Django 4.0.2 on 2022-07-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]