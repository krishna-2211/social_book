# Generated by Django 5.0 on 2024-01-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_customuser_fname_customuser_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='lname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
