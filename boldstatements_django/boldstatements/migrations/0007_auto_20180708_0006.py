# Generated by Django 2.0.5 on 2018-07-08 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boldstatements', '0006_auto_20180707_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='image',
            field=models.ImageField(blank=True, upload_to='documents/'),
        ),
    ]
