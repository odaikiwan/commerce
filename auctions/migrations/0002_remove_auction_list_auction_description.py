# Generated by Django 3.1.3 on 2020-11-09 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction_list',
            name='auction_description',
        ),
    ]
