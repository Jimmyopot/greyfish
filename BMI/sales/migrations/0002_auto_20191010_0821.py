# Generated by Django 2.2.5 on 2019-10-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='total',
            field=models.IntegerField(blank=True),
        ),
    ]
