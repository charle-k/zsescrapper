# Generated by Django 3.2.3 on 2021-06-15 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0002_zsedata_data_changed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zsedata',
            options={'ordering': ['-created'], 'verbose_name_plural': 'ZSEData'},
        ),
        migrations.AlterField(
            model_name='zsedata',
            name='data',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='zsedata',
            name='exported',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='zsedata',
            name='trading_date',
            field=models.DateField(null=True),
        ),
    ]
