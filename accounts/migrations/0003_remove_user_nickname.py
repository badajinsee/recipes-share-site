# Generated by Django 3.2.18 on 2023-05-24 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]
