# Generated by Django 3.1.5 on 2021-02-10 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0015_auto_20210211_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertprofile',
            name='Admin',
            field=models.BooleanField(default=False),
        ),
    ]
