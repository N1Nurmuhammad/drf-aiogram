# Generated by Django 4.1 on 2022-09-04 11:10

import comments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratinger', models.IntegerField()),
                ('whos_rating', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_photo', models.ImageField(upload_to=comments.models.upload_location)),
                ('full_name', models.TextField()),
                ('username', models.TextField()),
                ('phone_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
