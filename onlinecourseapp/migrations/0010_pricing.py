# Generated by Django 4.0.5 on 2022-06-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourseapp', '0009_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price1', models.IntegerField()),
            ],
        ),
    ]
