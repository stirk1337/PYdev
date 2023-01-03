# Generated by Django 4.1.4 on 2023-01-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4, verbose_name='Год')),
                ('salary', models.IntegerField(max_length=10, verbose_name='Уровень')),
                ('count', models.IntegerField(max_length=10, verbose_name='Количество')),
                ('salary_by_prof', models.IntegerField(max_length=10, verbose_name='Уровень (Python-программист)')),
                ('count_by_prof', models.IntegerField(max_length=10, verbose_name='Количество (Python-программист)')),
            ],
        ),
    ]