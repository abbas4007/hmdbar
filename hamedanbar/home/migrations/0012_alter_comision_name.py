# Generated by Django 5.0.2 on 2024-06-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_comision_aaza_comision_aaza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comision',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
