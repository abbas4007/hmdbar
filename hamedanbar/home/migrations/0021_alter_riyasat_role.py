# Generated by Django 5.0.2 on 2024-07-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_riyasat_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riyasat',
            name='role',
            field=models.CharField(max_length=50, unique=True, verbose_name='نقش'),
        ),
    ]