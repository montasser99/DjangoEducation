# Generated by Django 5.1.1 on 2024-10-16 23:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_remove_customuser_about_alter_customuser_avatar_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="about",
            field=models.TextField(blank=True, null=True),
        ),
    ]