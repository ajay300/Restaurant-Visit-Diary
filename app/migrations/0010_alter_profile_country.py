# Generated by Django 4.0.4 on 2022-05-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_diary_pic_alter_profile_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
