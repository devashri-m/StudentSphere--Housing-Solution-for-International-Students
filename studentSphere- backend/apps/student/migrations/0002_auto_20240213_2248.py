# Generated by Django 3.0.7 on 2024-02-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('userid', models.AutoField(db_column='userid', primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_column='first_name', max_length=45)),
                ('last_name', models.CharField(db_column='last_name', max_length=45)),
                ('email', models.CharField(db_column='email', max_length=45, unique=True)),
                ('contact', models.CharField(db_column='contact', max_length=45, null=True, unique=True)),
                ('college', models.CharField(db_column='college', max_length=45, null=True)),
                ('apartment', models.CharField(db_column='apartment', max_length=45, null=True)),
                ('password', models.CharField(db_column='password', max_length=45, unique=True)),
                ('active', models.BooleanField(db_column='active', default=True)),
            ],
            options={
                'db_table': 'student',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
