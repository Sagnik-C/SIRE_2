# Generated by Django 4.0.4 on 2022-06-18 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_gapanalysis'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='saved',
            field=models.CharField(default='no', max_length=50),
        ),
    ]
