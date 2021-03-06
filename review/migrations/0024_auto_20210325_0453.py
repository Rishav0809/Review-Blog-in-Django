# Generated by Django 2.0 on 2021-03-24 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0023_auto_20210325_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='imperfections',
            field=models.CharField(blank=True, default='No Imperfections', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='currency',
            field=models.CharField(blank=True, default='USD', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='maxprice',
            field=models.CharField(blank=True, default='0', max_length=100, null=True),
        ),
    ]
