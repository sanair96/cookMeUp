# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_auto_20170921_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='maj_ingredients',
            name='type_of_ingredient',
            field=models.CharField(choices=[('veg', 'Vegetable'), ('fruit', 'Fruit')], default='Vegetable', max_length=50),
        ),
        migrations.AlterField(
            model_name='maj_ingredients',
            name='name_of_ingredient',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
