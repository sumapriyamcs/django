# Generated by Django 3.2.10 on 2021-12-25 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='eemail',
        ),
    ]
