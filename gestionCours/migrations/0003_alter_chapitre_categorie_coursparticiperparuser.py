# Generated by Django 4.2 on 2024-10-30 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionCours', '0002_course_pdf_course_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapitre',
            name='categorie',
            field=models.CharField(blank=True, choices=[('Introduction', 'Introduction'), ('Les Bases', 'Les Bases'), ('Sujets Avancés', 'Sujets Avancés'), ('Études de Cas', 'Études de Cas'), ('Théorie', 'Théorie'), ('Applications Pratiques', 'Applications Pratiques'), ('Exercises', 'Exercices'), ('Résumé', 'Résumé'), ('Révision', 'Révision'), ('Travail de Projet', 'Travail de Projet'), ('Matériel Supplémentaire', 'Matériel Supplémentaire'), ('Exemples Concrets', 'Exemples Concrets'), ('Questions Fréquemment Posées (FAQ)', 'Questions Fréquemment Posées (FAQ)'), ('Meilleures Pratiques', 'Meilleures Pratiques'), ('Références', 'Références'), ('Ressources Complémentaires', 'Ressources Complémentaires'), ('Devoirs', 'Devoirs'), ('Laboratoires et Expériences', 'Laboratoires et Expériences'), ('Outils et Techniques', 'Outils et Techniques'), ('Conclusion', 'Conclusion')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='CoursParticiperParUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_participation', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_participations', to='gestionCours.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]