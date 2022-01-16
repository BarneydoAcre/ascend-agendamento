# Generated by Django 4.0 on 2022-01-16 00:29

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekly_day', models.IntegerField(choices=[(1, 'Domingo'), (2, 'Segunda-Feira'), (3, 'Terça-Feira'), (4, 'Quarta-Feira'), (5, 'Quinta-Feira'), (6, 'Sexta-Feira'), (7, 'Sábado')])),
                ('daily_hour', models.IntegerField(choices=[(1, '06 as 07'), (2, '07 as 08'), (3, '08 as 09'), (4, '09 as 10'), (5, '10 as 11'), (6, '11 as 12'), (7, '12 as 13'), (8, '13 as 14'), (9, '14 as 15'), (10, '15 as 16'), (11, '16 as 17'), (12, '17 as 18'), (13, '18 as 19'), (14, '19 as 20'), (15, '20 as 21'), (16, '21 as 22')])),
                ('busy', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=150)),
                ('image', models.FileField(blank=True, upload_to='app/static/public/service_images/')),
                ('price', models.FloatField()),
                ('sold_off', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('availability', models.ForeignKey(limit_choices_to={'busy': False}, on_delete=django.db.models.deletion.PROTECT, to='app.availability')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.person')),
            ],
        ),
    ]