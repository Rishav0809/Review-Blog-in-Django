# Generated by Django 3.1.5 on 2021-02-10 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0017_generatecode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generatecode',
            old_name='number',
            new_name='value',
        ),
    ]
