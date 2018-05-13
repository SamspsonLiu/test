# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-14 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challengemap',
            fields=[
                ('map_id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('hint', models.TextField(blank=True, null=True)),
                ('descr', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'challengemap',
            },
        ),
        migrations.CreateModel(
            name='Challengemapcontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'challengemapcontent',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('element_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('descr', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'element',
            },
        ),
        migrations.CreateModel(
            name='Freemap',
            fields=[
                ('map_id', models.AutoField(primary_key=True, serialize=False)),
                ('hint', models.TextField(blank=True, null=True)),
                ('descr', models.TextField(blank=True, null=True)),
                ('creator', models.IntegerField()),
                ('createdtime', models.DateTimeField(db_column='createdTime')),
                ('isrelease', models.IntegerField(blank=True, db_column='isRelease', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'freemap',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.SmallIntegerField(blank=True, null=True)),
                ('starttime', models.DateField()),
                ('endtime', models.DateField()),
            ],
            options={
                'managed': False,
                'db_table': 'membership',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=20)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('descr', models.TextField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Usercollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'usercollect',
            },
        ),
        migrations.CreateModel(
            name='Userentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('tel_number', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'managed': False,
                'db_table': 'userentry',
            },
        ),
        migrations.CreateModel(
            name='Userlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'userlike',
            },
        ),
        migrations.CreateModel(
            name='Usershare',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('map_id', models.IntegerField()),
                ('isfree', models.IntegerField(blank=True, db_column='isFree', null=True)),
                ('solution_code', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'usershare',
            },
        ),
    ]
