# Generated by Django 4.2.4 on 2023-08-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_student_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.IntegerField(blank=True, choices=[('100', '100'), ('200', '200'), ('300', '300'), ('400', '400')], null=True),
        ),
    ]