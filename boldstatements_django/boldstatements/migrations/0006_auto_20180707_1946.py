# Generated by Django 2.0.5 on 2018-07-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boldstatements', '0005_auto_20180706_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='image',
            field=models.ImageField(blank=True, height_field=350, upload_to='static/media/images'),
        ),
    ]
