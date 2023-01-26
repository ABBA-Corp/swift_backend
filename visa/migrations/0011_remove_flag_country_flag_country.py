# Generated by Django 4.1.2 on 2022-12-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0010_alter_flag_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flag',
            name='country',
        ),
        migrations.AddField(
            model_name='flag',
            name='country',
            field=models.ManyToManyField(blank=True, null=True, related_name='+', to='visa.countries'),
        ),
    ]
