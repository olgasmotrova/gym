# Generated by Django 4.1.6 on 2023-02-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datagym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(default='+380000000000', max_length=13, verbose_name='Contact us:'),
        ),
    ]
