# Generated by Django 5.0.2 on 2024-05-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_vakil_remove_article_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='وید\u200d\u200dیو'),
        ),
    ]
