# Generated by Django 2.2.6 on 2019-10-14 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191009_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='code',
            field=models.CharField(max_length=12),
        ),
    ]
