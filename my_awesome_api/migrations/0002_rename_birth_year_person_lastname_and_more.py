# Generated by Django 4.1.2 on 2022-10-20 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_awesome_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='birth_year',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='eye_color',
            new_name='nickname',
        ),
        migrations.RemoveField(
            model_name='person',
            name='species',
        ),
        migrations.DeleteModel(
            name='Species',
        ),
    ]