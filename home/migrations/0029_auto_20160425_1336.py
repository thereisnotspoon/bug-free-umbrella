# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-25 13:36
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20160425_0719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='form',
        ),
        migrations.RemoveField(
            model_name='contactpage',
            name='thank_you_text',
        ),
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.FormPage'),
        ),
    ]
