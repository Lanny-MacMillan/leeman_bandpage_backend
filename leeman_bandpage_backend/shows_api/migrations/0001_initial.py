# Generated by Django 4.0.5 on 2022-07-19 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.TextField(blank=True)),
                ('location', models.CharField(max_length=255)),
                ('coverPrice', models.IntegerField()),
                ('other', models.TextField(blank=True)),
            ],
        ),
    ]
