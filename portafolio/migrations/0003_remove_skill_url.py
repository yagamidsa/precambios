# Generated by Django 4.0.2 on 2022-02-20 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_remove_skill_web_remove_skill_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='url',
        ),
    ]
