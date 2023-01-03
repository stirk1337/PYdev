# Generated by Django 4.1.4 on 2023-01-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demand',
            options={'verbose_name': 'Статистика вакансий за год', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='demand',
            name='salary',
            field=models.IntegerField(max_length=10, verbose_name='Уровень зарплат'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='salary_by_prof',
            field=models.IntegerField(max_length=10, verbose_name='Уровень зарплат(Python-программист)'),
        ),
    ]
