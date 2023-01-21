from django.db import models


class Salary(models.Model):
    city = models.CharField('Город', max_length=15)
    value = models.IntegerField('Уровень зарплат')

    class Meta:
        verbose_name = 'Средняя зарплата в городе'
        verbose_name_plural = 'Средние зарплаты по городам'


class Proportion(models.Model):
    city = models.CharField('Город', max_length=15)
    value = models.CharField('Доля', max_length=10)

    class Meta:
        verbose_name = 'Доля вакансий в городе'
        verbose_name_plural = 'Доля вакансий по городам'


class Picture(models.Model):
    image = models.ImageField(upload_to='geography/static/geography/img', null=True, blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
