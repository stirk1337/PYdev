from django.db import models


class Text(models.Model):
    text = models.TextField('Текст', null=True)
    is_header = models.BooleanField('Заголовок', null=True)
    image = models.ImageField(upload_to='index/static/index/img', null=True, blank=True)
    has_picture = models.BooleanField('Есть картинка', null=True)

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'

