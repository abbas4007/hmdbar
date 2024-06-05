# Generated by Django 5.0.2 on 2024-05-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_studentdata_alter_vakil_thumbnail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentData',
        ),
        migrations.AlterField(
            model_name='vakil',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='vakil',
            name='code',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره پروانه'),
        ),
        migrations.AlterField(
            model_name='vakil',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انقضا'),
        ),
        migrations.AlterField(
            model_name='vakil',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'مرد'), ('F', 'زن')], max_length=1, null=True, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='vakil',
            name='lastname',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='vakil',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام'),
        ),
    ]