# Generated by Django 5.0.3 on 2024-03-23 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_data_list_main_id_alter_data_list_part_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_list',
            name='main_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.data_movie'),
        ),
    ]
