# Generated by Django 4.2.4 on 2023-08-25 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_room_room_status_alter_room_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
