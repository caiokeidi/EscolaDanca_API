# Generated by Django 3.1.5 on 2021-03-19 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=30)),
                ('descricao', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ImagemProfessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.professor')),
            ],
        ),
    ]
