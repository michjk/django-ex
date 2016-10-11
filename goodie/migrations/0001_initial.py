# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('code', models.CharField(max_length=200)),
                ('regex', models.TextField(default=b'(.*)')),
            ],
        ),
        migrations.CreateModel(
            name='Goodie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matric', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('event', models.ForeignKey(to='goodie.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matric', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='school',
            field=models.ManyToManyField(to='goodie.School'),
        ),
    ]
