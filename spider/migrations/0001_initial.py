# Generated by Django 3.2.3 on 2021-06-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZSEData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(editable=False, max_length=200)),
                ('trading_date', models.DateField(editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('exported', models.DateTimeField(editable=False, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]