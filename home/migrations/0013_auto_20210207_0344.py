# Generated by Django 3.1.5 on 2021-02-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210201_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metrics',
            options={'verbose_name': 'Метрики и виджеты для сайта'},
        ),
        migrations.AddField(
            model_name='metrics',
            name='widget',
            field=models.TextField(blank=True, null=True, verbose_name='Виджет'),
        ),
    ]
