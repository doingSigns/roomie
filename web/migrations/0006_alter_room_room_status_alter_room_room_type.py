# Generated by Django 4.2.4 on 2023-08-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_room_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_status',
            field=models.CharField(choices=[('available', 'Available'), ('not available', 'Not Available')], max_length=20),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('single', 'Single Room'), ('double', 'Double Room'), ('suite', 'Suite'), ('other', 'Other')], max_length=50),
        ),
    ]
