# Generated by Django 5.2 on 2025-06-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_grupohogar_codigo_invitacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupohogar',
            name='codigo_invitacion',
            field=models.CharField(default='74406201C2', max_length=10, unique=True),
        ),
    ]
