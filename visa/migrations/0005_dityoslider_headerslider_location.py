# Generated by Django 4.1.2 on 2022-11-21 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0004_countryslider_headerslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='DityoSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=2000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=2000, null=True)),
                ('link', models.CharField(blank=True, max_length=10000, null=True)),
                ('location', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='headerslider',
            name='location',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
