# Generated by Django 2.2 on 2019-05-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBVIApp', '0004_remove_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=None),
        ),
    ]