# Generated by Django 3.1.3 on 2021-01-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genres',
            field=models.CharField(choices=[('PP', 'POP'), ('RK', 'ROCK'), ('CL', 'CLASSIC'), ('ML', 'METAL')], default=0, max_length=2),
            preserve_default=False,
        ),
    ]
