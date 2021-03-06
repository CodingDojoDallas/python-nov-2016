# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CoursesApp', '0002_comments'),
        ('login_registration_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CoursesApp.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_registration_app.User')),
            ],
        ),
    ]
