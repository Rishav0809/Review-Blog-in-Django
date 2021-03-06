# Generated by Django 3.1.5 on 2021-02-09 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0008_delete_expertuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='expertprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='expertprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='review/images'),
        ),
        migrations.AlterField(
            model_name='expertprofile',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
