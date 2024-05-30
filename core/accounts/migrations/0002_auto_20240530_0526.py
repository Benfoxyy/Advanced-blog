# Generated by Django 3.2.25 on 2024-05-30 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]