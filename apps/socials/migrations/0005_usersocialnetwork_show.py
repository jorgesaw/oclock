# Generated by Django 2.2.13 on 2020-10-06 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0011_remove_show_social'),
        ('socials', '0004_auto_20201004_0347'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersocialnetwork',
            name='show',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shows.Show', verbose_name='show'),
            preserve_default=False,
        ),
    ]
