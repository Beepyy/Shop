# Generated by Django 3.2.6 on 2023-01-20 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LivelyHead', '0003_remove_good_parent_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='bought',
        ),
    ]
