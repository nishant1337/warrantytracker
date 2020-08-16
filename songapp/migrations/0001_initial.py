# Generated by Django 3.1 on 2020-08-14 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=100)),
                ('producttype', models.CharField(max_length=50)),
                ('purchasedate', models.DateField()),
                ('expirydate', models.DateField()),
                ('bill', models.ImageField(upload_to='images')),
                ('image', models.ImageField(upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]