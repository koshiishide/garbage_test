# Generated by Django 2.1 on 2019-12-13 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='code',
            new_name='amount_trash',
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='title',
            new_name='people',
        ),
    ]
