# Generated by Django 3.0.5 on 2020-08-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20200819_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_title',
            field=models.CharField(max_length=30),
        ),
    ]
