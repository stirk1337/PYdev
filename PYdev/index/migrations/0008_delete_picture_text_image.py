# Generated by Django 4.1.4 on 2023-01-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_remove_text_elems_remove_text_is_list'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.AddField(
            model_name='text',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='index/static/index/img'),
        ),
    ]
