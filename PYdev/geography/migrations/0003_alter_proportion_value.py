# Generated by Django 4.1.4 on 2023-01-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0002_alter_proportion_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proportion',
            name='value',
            field=models.CharField(max_length=10, verbose_name='Доля'),
        ),
    ]
