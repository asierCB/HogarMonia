# Generated by Django 5.2 on 2025-04-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_grupohogar_codigo_invitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupohogar',
            name='codigo_invitacion',
            field=models.CharField(default='3A93AFAF65', max_length=10, unique=True),
        ),
    ]
