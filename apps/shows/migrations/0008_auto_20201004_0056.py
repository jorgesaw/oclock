# Generated by Django 2.2.13 on 2020-10-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0007_auto_20200928_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=210, verbose_name='comment'),
        ),
    ]
