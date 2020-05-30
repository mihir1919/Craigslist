# Generated by Django 2.2.6 on 2020-05-29 17:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_item_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.date(2020, 5, 29))),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.item')),
            ],
        ),
    ]