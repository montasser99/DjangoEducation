# Generated by Django 4.2 on 2024-10-18 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_customuser_about"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "specialites",
                    models.CharField(
                        choices=[
                            ("Développement Web", "Développement Web"),
                            ("Développement Mobile", "Développement Mobile"),
                            ("Développement Logiciel", "Développement Logiciel"),
                            ("Développement Jeux Vidéo", "Développement Jeux Vidéo"),
                            ("Développement Réseau", "Développement Réseau"),
                            ("Développement Système", "Développement Système"),
                            ("Développement Embarqué", "Développement Embarqué"),
                            ("Développement IA", "Développement IA"),
                            ("Développement IoT", "Développement IoT"),
                            ("Développement Cloud", "Développement Cloud"),
                            ("Développement Big Data", "Développement Big Data"),
                            ("Développement Blockchain", "Développement Blockchain"),
                            ("Développement Sécurité", "Développement Sécurité"),
                            ("Développement DevOps", "Développement DevOps"),
                            ("Développement Autre", "Développement Autre"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "niveau",
                    models.CharField(
                        choices=[
                            ("Débutant", "Débutant"),
                            ("Intermédiaire", "Intermédiaire"),
                            ("Avancé", "Avancé"),
                        ],
                        default="Débutant",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="courses/images/"
                    ),
                ),
                (
                    "pdf",
                    models.FileField(blank=True, null=True, upload_to="courses/pdfs/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserLoginAttempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("ip_address", models.GenericIPAddressField()),
                ("successful", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAlert",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("is_read", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CoursParticiperParUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_participation", models.DateTimeField(auto_now_add=True)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.course",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]