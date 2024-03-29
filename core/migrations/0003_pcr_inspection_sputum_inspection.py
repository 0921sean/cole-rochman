# Generated by Django 2.2.8 on 2022-10-03 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221003_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sputum_Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_res', models.CharField(choices=[('+1', '+1'), ('+2', '+2'), ('+3', '+3'), ('+4', '+4'), ('-', '-')], max_length=20)),
                ('positive_negative', models.CharField(choices=[('결핵균 양성', '결핵균 양성'), ('결핵균 음성', '결핵균 음성'), ('검사중', '검사중')], max_length=40)),
                ('date', models.DateField(null=True)),
                ('patient_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Pcr_Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_res', models.CharField(choices=[('양성', '양성'), ('음성', '음성')], max_length=20)),
                ('patient_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
        ),
    ]
