from django.db import models


class Demand(models.Model):
    year = models.IntegerField('Год')
    salary = models.IntegerField('Уровень зарплат')
    count = models.IntegerField('Количество')
    salary_by_prof = models.IntegerField('Уровень зарплат(Python-программист)')
    count_by_prof = models.IntegerField('Количество (Python-программист)')

    class Meta:
        verbose_name = 'Статистика вакансий за год'
        verbose_name_plural = 'Вакансии'


class Picture(models.Model):
    image = models.ImageField(upload_to='demand/static/demand/img', null=True, blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
