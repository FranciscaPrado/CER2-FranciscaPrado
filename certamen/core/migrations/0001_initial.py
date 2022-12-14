# Generated by Django 4.1.2 on 2022-11-13 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conserje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('primer_apellido', models.CharField(max_length=30)),
                ('segundo_apellido', models.CharField(max_length=30)),
                ('fono', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='residencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_res', models.CharField(max_length=30)),
                ('dueño_res', models.CharField(max_length=30)),
                ('fono_dueño', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recepcion', models.DateField()),
                ('conserje', models.CharField(max_length=30)),
                ('remitente', models.CharField(max_length=30)),
                ('destinatario', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('numero_res', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.residencia')),
            ],
        ),
    ]
