# Generated by Django 4.1.1 on 2022-10-07 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_role_staff_user_role_course_skills_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrole',
            name='Staff_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.staff'),
        ),
    ]
