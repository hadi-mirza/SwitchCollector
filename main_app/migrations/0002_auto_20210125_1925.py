# Generated by Django 3.1.3 on 2021-01-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
