# Generated by Django 4.1.1 on 2022-10-01 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESchoolVR', '0007_rename_name_student_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]