# Generated by Django 5.0 on 2024-01-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_remove_customuser_fname_remove_customuser_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fname',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lname',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
