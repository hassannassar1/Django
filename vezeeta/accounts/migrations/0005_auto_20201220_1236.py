# Generated by Django 3.1.3 on 2020-12-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الكشف'),
        ),
    ]
