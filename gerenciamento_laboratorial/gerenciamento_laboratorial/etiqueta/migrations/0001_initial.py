# Generated by Django 5.0.9 on 2024-09-30 23:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=50, verbose_name='Código')),
                ('tipo_exame', models.CharField(blank=True, max_length=50, verbose_name='Tipo de Exame')),
                ('data_coleta', models.DateField(blank=True, null=True, verbose_name='Data da Coleta')),
                ('hora_coleta', models.CharField(blank=True, max_length=50, verbose_name='Horário da Coleta')),
            ],
        ),
    ]
