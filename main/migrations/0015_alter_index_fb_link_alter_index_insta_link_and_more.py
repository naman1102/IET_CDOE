# Generated by Django 4.0.4 on 2022-06-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_index_address_alter_index_contact_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='fb_link',
            field=models.URLField(default='#', null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='insta_link',
            field=models.URLField(default='#', null=True),
        ),
        migrations.AlterField(
            model_name='index',
            name='twitter_link',
            field=models.URLField(default='#', null=True),
        ),
    ]