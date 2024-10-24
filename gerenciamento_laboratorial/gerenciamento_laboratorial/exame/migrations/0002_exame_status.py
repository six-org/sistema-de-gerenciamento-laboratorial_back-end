# Generated by Django 5.0.9 on 2024-10-24 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exame',
            name='status',
            field=models.CharField(choices=[('AGENDAMENTO', 'Esperando confirmação dos técnicos'), ('AGENDADO', 'Exame agendado'), ('CANCELAMENTO', 'Cancelamento solicitado')], default='AGENDAMENTO', max_length=20),
        ),
    ]
