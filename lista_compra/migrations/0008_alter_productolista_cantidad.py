# Generated by Django 5.2 on 2025-06-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista_compra', '0007_alter_productolista_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productolista',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
