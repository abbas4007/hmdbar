# Generated by Django 5.0.2 on 2024-06-03 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_vakil_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Riyasat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, verbose_name='نقش')),
                ('vakil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vakils', to='home.vakil', verbose_name='وکیل')),
            ],
        ),
    ]