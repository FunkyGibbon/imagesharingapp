# Generated by Django 3.0.6 on 2020-05-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapi', '0003_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='dateuploaded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
