# Generated by Django 3.2.12 on 2022-02-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220211_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(null=True),
        ),
        migrations.AlterField(
            model_name='technology',
            name='logo',
            field=models.FilePathField(),
        ),
    ]
