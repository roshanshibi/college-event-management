# Generated by Django 3.2.4 on 2021-07-27 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='f_email',
            new_name='femail',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='f_name',
            new_name='fname',
        ),
    ]
