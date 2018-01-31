# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-31 14:48
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_auto_20180131_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='intern_tasks',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) Description of possible internship tasks.', max_length=3000),
        ),
    ]
