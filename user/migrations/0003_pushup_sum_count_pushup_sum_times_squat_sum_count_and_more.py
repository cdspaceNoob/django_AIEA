# Generated by Django 4.0 on 2021-12-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_bicepscurl_sum_count_bicepscurl_sum_times_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pushup',
            name='sum_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pushup',
            name='sum_times',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='squat',
            name='sum_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='squat',
            name='sum_times',
            field=models.IntegerField(null=True),
        ),
    ]
