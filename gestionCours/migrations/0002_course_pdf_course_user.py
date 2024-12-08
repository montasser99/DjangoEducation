# Generated by Django 5.1.1 on 2024-10-27 01:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestionCours", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="pdf",
            field=models.FileField(blank=True, null=True, upload_to="courses/pdfs/"),
        ),
        migrations.AddField(
            model_name="course",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enseignant_courses",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]