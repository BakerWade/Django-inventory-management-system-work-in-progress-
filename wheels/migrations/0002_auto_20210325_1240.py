# Generated by Django 3.1.7 on 2021-03-25 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wheels', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wheels',
            new_name='WheelPart',
        ),
    ]