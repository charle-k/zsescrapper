# Generated by Django 3.2.3 on 2022-04-21 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0004_alter_zsedata_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zsedata',
            options={'ordering': ['-created'], 'verbose_name_plural': 'ZSE Data'},
        ),
    ]
