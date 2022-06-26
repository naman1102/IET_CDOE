# Generated by Django 4.0.4 on 2022-06-26 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_index_fb_link_alter_index_insta_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='num_of_online_courses',
            field=models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
