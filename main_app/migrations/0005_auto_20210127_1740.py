# Generated by Django 3.1.3 on 2021-01-27 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210127_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='reviews',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
