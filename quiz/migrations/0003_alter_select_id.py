# Generated by Django 3.2.9 on 2021-11-25 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20211125_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='select',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
