# Generated by Django 4.2.7 on 2023-11-17 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taggeditem',
            old_name='contentType',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='taggeditem',
            old_name='objectId',
            new_name='object_id',
        ),
    ]
