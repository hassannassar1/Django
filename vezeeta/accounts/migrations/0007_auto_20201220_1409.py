# Generated by Django 3.1.3 on 2020-12-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201220_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(default='', max_length=15, verbose_name='العنوان بالتفصيل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default='', max_length=14, verbose_name='رقم الموبايل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='specialization',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='التخصص'),
        ),
        migrations.AddField(
            model_name='profile',
            name='subtitle',
            field=models.CharField(default='', max_length=50, verbose_name='نبذة عنك'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='waiting_hours',
            field=models.IntegerField(default=2, verbose_name='عدد ساعات الإنتظار'),
        ),
        migrations.AddField(
            model_name='profile',
            name='working_hours',
            field=models.CharField(default='', max_length=2, verbose_name='عدد ساعات العمل'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=15, verbose_name='المحافظة'),
        ),
    ]
