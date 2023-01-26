# Generated by Django 4.1.2 on 2022-12-04 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0006_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Continents',
            },
        ),
        migrations.AlterModelOptions(
            name='buisnesscategory',
            options={'verbose_name_plural': 'Buisness Category'},
        ),
        migrations.AlterModelOptions(
            name='citizencategory',
            options={'verbose_name_plural': 'Citizen Category'},
        ),
        migrations.AlterModelOptions(
            name='countries',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='countryslider',
            options={'verbose_name_plural': 'Country Slider'},
        ),
        migrations.AlterModelOptions(
            name='dityoslider',
            options={'verbose_name_plural': 'Dityo Slider'},
        ),
        migrations.AlterModelOptions(
            name='headerslider',
            options={'verbose_name_plural': 'Header Slider'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='travel',
            options={'verbose_name_plural': 'Travel'},
        ),
        migrations.AlterModelOptions(
            name='unnecessary',
            options={'verbose_name_plural': 'Unnecessary'},
        ),
        migrations.AlterModelOptions(
            name='visacategory',
            options={'verbose_name_plural': 'Visa Category'},
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visa.continent')),
            ],
            options={
                'verbose_name_plural': 'Flags',
            },
        ),
    ]
