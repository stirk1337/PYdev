# Generated by Django 4.1.4 on 2023-01-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]