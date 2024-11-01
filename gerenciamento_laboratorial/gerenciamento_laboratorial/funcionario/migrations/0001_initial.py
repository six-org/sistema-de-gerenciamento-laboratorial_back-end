# Generated by Django 5.0.9 on 2024-10-24 17:07

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome_completo', models.CharField(max_length=255)),
                ('cpf', models.CharField(default='000.000.000-00', max_length=14, unique=True)),
                ('data_nascimento', models.DateField()),
                ('cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('nivel_acesso', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
