# Generated by Django 3.2.8 on 2022-07-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_data_bat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ET0',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time_Stamp', models.DateTimeField(auto_now_add=True)),
                ('value', models.FloatField()),
                ('WSavg', models.FloatField()),
                ('ewTmoy', models.FloatField()),
                ('ewTmin', models.FloatField()),
                ('ewTmax', models.FloatField()),
                ('ew', models.FloatField()),
                ('e', models.FloatField()),
                ('U2', models.FloatField()),
                ('Delta', models.FloatField()),
            ],
        ),
    ]
