# Generated by Django 2.2 on 2019-05-22 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CBVIApp', '0003_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]