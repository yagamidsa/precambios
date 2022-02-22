# Generated by Django 4.0.2 on 2022-02-17 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
                ('date', models.DateTimeField(verbose_name=datetime.date.today)),
            ],
        ),
    ]