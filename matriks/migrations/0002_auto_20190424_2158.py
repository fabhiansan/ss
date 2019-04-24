# Generated by Django 2.1 on 2019-04-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rci',
            name='month',
            field=models.CharField(choices=[('Januari', 'Januari'), ('Februari', 'Februari')], default='Januari', max_length=10),
        ),
        migrations.AddField(
            model_name='rci',
            name='years',
            field=models.CharField(choices=[('2018', '2018'), ('2019', '2019')], default='2018', max_length=10),
        ),
        migrations.AlterField(
            model_name='rci',
            name='segmen',
            field=models.CharField(choices=[('KM 75', 'KM 75'), ('KM 75.5', 'KM75.5')], max_length=10),
        ),
        migrations.DeleteModel(
            name='segmenRCI',
        ),
    ]
