# Generated by Django 4.1.2 on 2022-10-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
