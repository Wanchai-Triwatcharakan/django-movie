# Generated by Django 5.0.3 on 2024-03-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_remove_data_list_name_alter_data_list_main_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_list',
            name='name',
            field=models.TextField(null=True),
        ),
    ]