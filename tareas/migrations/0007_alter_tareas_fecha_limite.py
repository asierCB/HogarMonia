# Generated by Django 5.2 on 2025-06-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0006_alter_tareas_participantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='fecha_limite',
            field=models.DateField(blank=True, null=True),
        ),
    ]
