# Generated by Django 3.1.1 on 2020-11-08 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20201108_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairs',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
