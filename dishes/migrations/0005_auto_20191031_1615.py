# Generated by Django 2.2.6 on 2019-10-31 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0004_auto_20191031_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='add_type',
            new_name='type',
        ),
    ]
