# Generated by Django 3.2.9 on 2021-11-27 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_select_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='select',
            name='user',
        ),
    ]
