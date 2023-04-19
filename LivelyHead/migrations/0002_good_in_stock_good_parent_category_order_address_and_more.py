# Generated by Django 4.0.3 on 2022-12-22 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LivelyHead', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='in_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='good',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='LivelyHead.good'),
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
