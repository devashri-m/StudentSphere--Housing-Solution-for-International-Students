# Generated by Django 3.0.7 on 2024-04-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20240326_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='contact',
            field=models.CharField(db_column='contact', max_length=255, null=True, unique=True),
        ),
    ]
