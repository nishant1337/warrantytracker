# Generated by Django 3.1 on 2020-08-14 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songapp', '0004_bills_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bills',
            old_name='invoice',
            new_name='bill',
        ),
    ]
