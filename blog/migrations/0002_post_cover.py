# Generated by Django 3.1.4 on 2021-02-07 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/'),
            preserve_default=False,
        ),
    ]
