# Generated by Django 2.2.8 on 2023-11-30 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_patient_remind_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom_name', models.TextField()),
                ('medication_result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='side_effects', to='core.MedicationResult')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationTimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_time', models.TimeField(blank=True, default=None, null=True, verbose_name='복약알림 시간')),
                ('activate', models.BooleanField(default=True, verbose_name='알림 활성화 여부')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notification_time_tables', to='core.Patient')),
            ],
        ),
    ]