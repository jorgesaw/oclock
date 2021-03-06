# Generated by Django 2.2.13 on 2020-06-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200608_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_consumer',
            field=models.BooleanField(default=False, help_text='Help easily distinguish users client and consumer and perform queries.', verbose_name='consumer'),
        ),
    ]
