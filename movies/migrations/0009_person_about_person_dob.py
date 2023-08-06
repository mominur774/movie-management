# Generated by Django 4.2.3 on 2023-08-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_movietype_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
