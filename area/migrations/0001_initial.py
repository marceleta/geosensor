# Generated by Django 4.0.3 on 2022-05-07 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateField(auto_now=True, verbose_name='modificado em')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('descricao', models.CharField(default='', max_length=300, null=True, verbose_name='descrição')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateField(auto_now=True, verbose_name='modificado em')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('a_rea', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='area.area')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateField(auto_now=True, verbose_name='modificado em')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('centro_area', models.BooleanField(null=True)),
                ('area', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='area.area')),
                ('rua', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='area.rua')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
