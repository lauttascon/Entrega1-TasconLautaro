# Generated by Django 4.1 on 2022-09-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_entregable_estudiante_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipoFutbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fechaNacimiento', models.DateField()),
                ('pais', models.CharField(max_length=60)),
                ('titulos', models.PositiveIntegerField(default=0)),
                ('mejorJugador', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='EstadioFutbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('ubicacion', models.CharField(max_length=60)),
                ('fechaInauguracion', models.DateField()),
                ('capacidad', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='JugadorFutbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('nacionalidad', models.CharField(max_length=60)),
                ('edad', models.PositiveIntegerField(default=0)),
                ('posicion', models.CharField(max_length=60)),
                ('dorsal', models.PositiveIntegerField(default=0)),
                ('piernaHabil', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
