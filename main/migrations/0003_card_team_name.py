# Generated by Django 2.2.4 on 2020-09-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200904_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='team_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]