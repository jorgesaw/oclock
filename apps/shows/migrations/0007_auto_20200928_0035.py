# Generated by Django 2.2.13 on 2020-09-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='rate',
            field=models.SmallIntegerField(default=1, verbose_name='rate'),
        ),
        migrations.AddField(
            model_name='show',
            name='views',
            field=models.IntegerField(default=0, verbose_name='views'),
        ),
    ]
