# Generated by Django 4.2.5 on 2023-09-11 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_movie_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='pages',
            field=models.IntegerField(null=True),
        ),
    ]