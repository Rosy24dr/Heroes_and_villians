# Generated by Django 4.0.3 on 2022-04-06 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0002_rename_super_type_supertype_super_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supertype',
            old_name='Super_type',
            new_name='super_type',
        ),
    ]