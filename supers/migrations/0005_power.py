# Generated by Django 4.0.3 on 2022-04-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0004_rename_super_type_id_super_super_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
