# Generated by Django 3.1.3 on 2020-12-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20201220_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(choices=[('جلدية', 'جلدية'), ('أسنان', 'أسنان'), ('باطنة', 'باطنة'), ('قلب', 'قلب'), ('جراحة', 'جراحة'), ('مخ وأعصاب', 'مخ وأعصاب'), ('نفسية', 'نفسية'), ('أنف وأذن وحنجرة', 'أنف وأذن وحنجرة'), ('عيون', 'عيون'), ('عظام', 'عظام'), ('أطفال', 'أطفال'), ('صدر', 'صدر')], max_length=30, verbose_name='دكتور؟'),
        ),
    ]
