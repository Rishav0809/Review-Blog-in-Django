# Generated by Django 2.0 on 2021-03-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0024_auto_20210325_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertprofile',
            name='Credits',
            field=models.PositiveIntegerField(blank=True, default=5),
        ),
    ]
