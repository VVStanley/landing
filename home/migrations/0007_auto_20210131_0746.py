# Generated by Django 3.1.5 on 2021-01-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_mainblock_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainblock',
            name='alt',
            field=models.CharField(max_length=200, verbose_name='Описание картинки - АЛЬТ'),
        ),
    ]
