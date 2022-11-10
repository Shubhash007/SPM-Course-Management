# Generated by Django 4.1.1 on 2022-11-09 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_rename_course_requirements_course_registered"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job_role",
            name="Dept",
            field=models.CharField(
                default="",
                max_length=30,
                validators=[
                    django.core.validators.MaxLengthValidator(
                        30, message="Between 0 and 30"
                    )
                ],
            ),
        ),
    ]