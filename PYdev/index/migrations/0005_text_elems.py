# Generated by Django 4.1.4 on 2023-01-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_text_is_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='elems',
            field=models.TextField(null=True, verbose_name='Перечисление(через запятую)'),
        ),
    ]
