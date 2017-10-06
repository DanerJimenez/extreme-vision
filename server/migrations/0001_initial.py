# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-06 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.DecimalField(decimal_places=20, max_digits=30)),
                ('y', models.DecimalField(decimal_places=20, max_digits=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('gps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Gps')),
            ],
        ),
    ]