# Generated by Django 2.1.4 on 2019-01-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_events_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
