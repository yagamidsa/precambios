# Generated by Django 4.0.2 on 2022-02-20 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0004_rename_title_skill_carrera_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='descripcion',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
    ]
