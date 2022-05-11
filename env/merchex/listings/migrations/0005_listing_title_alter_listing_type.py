# Generated by Django 4.0.4 on 2022-04-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('R', 'Records'), ('C', 'Clothing'), ('P', 'Posters'), ('M', 'Miscellaneous')], max_length=5),
        ),
    ]