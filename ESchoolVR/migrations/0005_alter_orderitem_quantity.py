# Generated by Django 4.1.1 on 2022-09-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESchoolVR', '0004_remove_course_teacher_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]