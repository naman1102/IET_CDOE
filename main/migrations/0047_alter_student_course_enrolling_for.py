# Generated by Django 4.0.4 on 2022-06-24 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_alter_student_course_enrolling_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_enrolling_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course_head'),
        ),
    ]