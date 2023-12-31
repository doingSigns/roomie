# Generated by Django 4.2.4 on 2023-08-17 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_student_first_name_remove_student_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='preferences',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.AddField(
            model_name='preference',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.CreateModel(
            name='PreferenceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100)),
                ('preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.preference')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='preferences',
            field=models.ManyToManyField(to='web.preferenceoption'),
        ),
    ]
