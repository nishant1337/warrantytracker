# Generated by Django 3.1 on 2020-08-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songapp', '0003_remove_bills_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='logo',
            field=models.ImageField(default='"/media/images/s.png', upload_to='images'),
        ),
    ]