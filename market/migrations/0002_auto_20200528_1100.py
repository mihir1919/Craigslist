# Generated by Django 2.2.6 on 2020-05-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='item',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]