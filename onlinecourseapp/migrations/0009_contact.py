# Generated by Django 4.0.5 on 2022-06-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourseapp', '0008_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
