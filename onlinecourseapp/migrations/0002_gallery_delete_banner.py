# Generated by Django 4.0.5 on 2022-06-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_img1', models.ImageField(upload_to='images')),
                ('gallery_img1_i', models.ImageField(upload_to='images')),
                ('gallery_img2', models.ImageField(upload_to='images')),
                ('gallery_img2_i', models.ImageField(upload_to='images')),
                ('gallery_img3', models.ImageField(upload_to='images')),
                ('gallery_img3_i', models.ImageField(upload_to='images')),
                ('gallery_img4', models.ImageField(upload_to='images')),
                ('gallery_img4_i', models.ImageField(upload_to='images')),
                ('gallery_img5', models.ImageField(upload_to='images')),
                ('gallery_img5_i', models.ImageField(upload_to='images')),
                ('gallery_img6', models.ImageField(upload_to='images')),
                ('gallery_img6_i', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='banner',
        ),
    ]
