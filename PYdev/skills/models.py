from django.db import models


class Skill(models.Model):
    year = models.IntegerField('Год')
    skill1 = models.CharField('Навык 1', max_length=20)
    skill1_count = models.IntegerField('Количество повторений')
    skill2 = models.CharField('Навык 2', max_length=20)
    skill2_count = models.IntegerField('Количество повторений')
    skill3 = models.CharField('Навык 3', max_length=20)
    skill3_count = models.IntegerField('Количество повторений')
    skill4 = models.CharField('Навык 4', max_length=20)
    skill4_count = models.IntegerField('Количество повторений')
    skill5 = models.CharField('Навык 5', max_length=20)
    skill5_count = models.IntegerField('Количество повторений')
    skill6 = models.CharField('Навык 6', max_length=20)
    skill6_count = models.IntegerField('Количество повторений')
    skill7 = models.CharField('Навык 7', max_length=20)
    skill7_count = models.IntegerField('Количество повторений')
    skill8 = models.CharField('Навык 8', max_length=20)
    skill8_count = models.IntegerField('Количество повторений')
    skill9 = models.CharField('Навык 9', max_length=20)
    skill9_count = models.IntegerField('Количество повторений')
    skill10 = models.CharField('Навык 10', max_length=20)
    skill10_count = models.IntegerField('Количество повторений')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
