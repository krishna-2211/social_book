# Generated by Django 5.0 on 2024-01-06 04:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_remove_uploadedfile_user_alter_uploadedfile_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]