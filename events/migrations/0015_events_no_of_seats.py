# Generated by Django 3.2.4 on 2021-09-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='no_of_seats',
            field=models.IntegerField(null=True),
        ),
    ]