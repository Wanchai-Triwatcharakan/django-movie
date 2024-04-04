# Generated by Django 5.0.3 on 2024-03-26 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_rename_img_data_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_list',
            name='name',
        ),
        migrations.AlterField(
            model_name='data_list',
            name='main_id',
            field=models.ForeignKey(limit_choices_to={'status_list': 'yes'}, on_delete=django.db.models.deletion.CASCADE, to='movie.data_movie'),
        ),
    ]
