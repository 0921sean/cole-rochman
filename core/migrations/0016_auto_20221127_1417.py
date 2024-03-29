# Generated by Django 2.2.8 on 2022-11-27 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20221127_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='vision_left',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='왼쪽 시력'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='vision_right',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name=' 오른쪽 시력'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='몸무게'),
        ),
    ]
