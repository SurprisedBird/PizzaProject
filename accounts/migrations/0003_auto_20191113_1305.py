# Generated by Django 2.2.7 on 2019-11-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191112_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='ac01c37ece51455ebde480e6c4f9a00a8947f33f6f3b4189878585771afcbc36', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='bd2a0a419f9948f99170dbeffadffcd56fc20e9b46ca43c78b35d23557503d9c', max_length=300, null=True),
        ),
    ]
