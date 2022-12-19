# Generated by Django 4.1.1 on 2022-12-19 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seminario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('fechaInscripcion', models.DateField()),
                ('horaInscripcion', models.TimeField()),
                ('estados', models.CharField(choices=[['RESERVADO', 'RESERVADO'], ['COMPLETADA', 'COMPLETADA'], ['ANULADA', 'ANULADA'], ['NO ASISTEN', 'NO ASISTEN']], max_length=50)),
                ('observacion', models.CharField(blank=True, max_length=50)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test3y4.institucion')),
            ],
        ),
    ]
