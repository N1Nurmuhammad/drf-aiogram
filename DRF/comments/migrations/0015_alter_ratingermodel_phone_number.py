# Generated by Django 4.1 on 2022-10-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0014_alter_usermodel_photo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingermodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]