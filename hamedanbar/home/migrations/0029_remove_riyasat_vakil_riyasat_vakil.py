# Generated by Django 5.0.2 on 2024-08-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_remove_riyasat_name_riyasat_vakil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riyasat',
            name='vakil',
        ),
        migrations.AddField(
            model_name='riyasat',
            name='vakil',
            field=models.ManyToManyField(blank=True, null=True, to='home.vakil'),
        ),
    ]
