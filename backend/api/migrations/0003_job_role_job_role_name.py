# Generated by Django 4.1.1 on 2022-10-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_requirements_job_role_alter_requirements_skill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_role',
            name='Job_Role_Name',
            field=models.CharField(default='', max_length=20),
        ),
    ]