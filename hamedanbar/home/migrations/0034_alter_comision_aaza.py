# Generated by Django 4.2.16 on 2024-11-12 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_comision_aaza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comision',
            name='aaza',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.vakil'),
        ),
    ]