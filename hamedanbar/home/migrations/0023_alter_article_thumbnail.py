# Generated by Django 5.0.2 on 2024-08-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_articleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(upload_to='image', verbose_name='تصویر مقاله'),
        ),
    ]