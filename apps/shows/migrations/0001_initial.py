# Generated by Django 2.2.13 on 2020-09-20 19:47

import apps.utils.images.uploads_images
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0002_auto_20200419_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('name', models.CharField(error_messages={'unique': 'A event with that name already exists.'}, max_length=210, unique=True, verbose_name='event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('fantasy_name', models.CharField(error_messages={'unique': 'A user with that show already exists.'}, max_length=210, unique=True, verbose_name='fantasy name')),
                ('description', models.TextField(blank=True, max_length=3500, null=True)),
                ('scope_show', models.CharField(choices=[('Sólo en mi localidad', 'Sólo en mi localidad'), ('Sólo en mi zona', 'Sólo en mi zona'), ('En todo el país', 'En todo el país')], default='Sólo en mi localidad', max_length=25, verbose_name='offer show')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=apps.utils.images.uploads_images.custom_upload_to, verbose_name='show picture')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.City', verbose_name='location')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shows.Event', verbose_name='Event type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
