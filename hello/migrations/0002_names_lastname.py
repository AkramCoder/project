# Generated by Django 2.1 on 2019-12-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='names',
            name='lastname',
            field=models.CharField(default='akeblersane', max_length=150),
        ),
    ]
