# Generated by Django 3.0.6 on 2020-06-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostposts', '0003_auto_20200617_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='submission_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
