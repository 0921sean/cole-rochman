# Generated by Django 2.2.8 on 2022-10-22 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20221023_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
    ]