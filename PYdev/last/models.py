from django.db import models


class Text(models.Model):
    text = models.TextField('Текст', null=True)
    type = models.PositiveSmallIntegerField('Тип', choices=[(1, 'h1'), (2, 'h2'), (3, 'p')], null=True)
    image = models.ImageField(upload_to='last/static/last/img', null=True, blank=True)
    has_picture = models.BooleanField('Есть картинка', null=True)

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'