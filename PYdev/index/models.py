from django.db import models


class Text(models.Model):
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'


class Picture(models.Model):
    image = models.ImageField(upload_to='index/static/index/img', null=True, blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
