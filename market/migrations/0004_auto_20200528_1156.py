# Generated by Django 2.2.6 on 2020-05-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20200528_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('car', 'CAR'), ('home', 'Furniture'), ('education', 'EDUCATION'), ('electronics', 'ELECTRONICS'), ('misc', 'MISC')], default='misc', max_length=100),
        ),
    ]
