# Generated by Django 4.0.4 on 2022-05-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_chapter_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(choices=[('India', 'India'), ('Czechia', 'czechia'), ('Asia', 'Asia')], max_length=15),
        ),
    ]
