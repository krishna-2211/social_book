# Generated by Django 5.0 on 2024-01-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customuser_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fname',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lname',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
