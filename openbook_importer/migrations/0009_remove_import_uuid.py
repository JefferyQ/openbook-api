# Generated by Django 2.1.5 on 2019-02-09 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_importer', '0008_import_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='import',
            name='uuid',
        ),
    ]