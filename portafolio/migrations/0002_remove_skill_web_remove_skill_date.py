# Generated by Django 4.0.2 on 2022-02-20 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='Web',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='date',
        ),
    ]
