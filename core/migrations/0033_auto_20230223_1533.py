# Generated by Django 2.2.8 on 2023-02-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20230208_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sputum_inspection',
            name='positive_negative',
            field=models.CharField(choices=[('양성', '양성'), ('음성', '음성'), ('검사중', '검사중')], max_length=40, verbose_name='양성/음성'),
        ),
    ]
