# Generated by Django 5.0.6 on 2024-06-26 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quote',
            new_name='Quotes',
        ),
    ]