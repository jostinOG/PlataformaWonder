# Generated by Django 4.0.1 on 2022-01-20 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wonder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='psicologo', to=settings.AUTH_USER_MODEL),
        ),
    ]
