# Generated by Django 5.0.3 on 2024-03-23 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_data_list_main_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_movie',
            old_name='images',
            new_name='image',
        ),
    ]