# Generated by Django 4.0.3 on 2022-12-22 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LivelyHead', '0002_good_in_stock_good_parent_category_order_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='parent_category',
        ),
        migrations.AddField(
            model_name='goodcategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='LivelyHead.goodcategory'),
        ),
    ]
