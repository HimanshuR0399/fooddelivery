# Generated by Django 3.2.7 on 2021-10-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddelivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foods',
            name='prise',
            field=models.IntegerField(default=0),
        ),
    ]