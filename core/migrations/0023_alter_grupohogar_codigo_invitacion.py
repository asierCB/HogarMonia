# Generated by Django 5.2 on 2025-05-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_grupohogar_codigo_invitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupohogar',
            name='codigo_invitacion',
            field=models.CharField(default='6C7DA2A2D6', max_length=10, unique=True),
        ),
    ]
