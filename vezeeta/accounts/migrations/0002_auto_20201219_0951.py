# Generated by Django 3.1.3 on 2020-12-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(verbose_name='سعر الكشف'),
        ),
    ]
