# Generated by Django 4.1.1 on 2022-10-16 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                ("Skill_ID", models.IntegerField(primary_key=True, serialize=False)),
                ("Skill_Name", models.CharField(max_length=50)),
                ("Skill_Desc", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Skills",
            },
        ),
        migrations.CreateModel(
            name="User_Role",
            fields=[
                (
                    "User_Role_ID",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("User_Role_Name", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name_plural": "User_Roles",
            },
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                ("Staff_ID", models.BigIntegerField(primary_key=True, serialize=False)),
                ("Staff_FName", models.CharField(max_length=50)),
                ("Staff_LName", models.CharField(max_length=50)),
                ("Dept", models.CharField(max_length=50)),
                ("Email", models.EmailField(max_length=50)),
                (
                    "User_Role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.user_role"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Staffs",
            },
        ),
        migrations.CreateModel(
            name="Job_Role",
            fields=[
                ("Job_Role_ID", models.IntegerField(primary_key=True, serialize=False)),
                ("Job_Role_Name", models.CharField(default="", max_length=20)),
                ("Job_Role_Desc", models.CharField(max_length=255)),
                ("Skills", models.ManyToManyField(to="api.skill")),
            ],
            options={
                "verbose_name_plural": "Job_Roles",
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "Course_ID",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("Course_Name", models.CharField(max_length=50)),
                ("Course_Desc", models.CharField(max_length=255)),
                ("Course_Status", models.CharField(max_length=15)),
                ("Course_Type", models.CharField(max_length=10)),
                ("Course_Category", models.CharField(max_length=50)),
                ("Skills", models.ManyToManyField(to="api.skill")),
            ],
            options={
                "verbose_name_plural": "Courses",
            },
        ),
        migrations.CreateModel(
            name="Requirements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.course"
                    ),
                ),
                (
                    "Job_Role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.job_role"
                    ),
                ),
                (
                    "Staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.staff"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Requirements",
                "managed": True,
                "unique_together": {("Course", "Job_Role", "Staff")},
            },
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                ("Reg_ID", models.IntegerField(primary_key=True, serialize=False)),
                ("Reg_Status", models.CharField(default="", max_length=20, null=True)),
                (
                    "Completion_Status",
                    models.CharField(default="", max_length=20, null=True),
                ),
                (
                    "Course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.course"
                    ),
                ),
                (
                    "Staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.staff"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Registrations",
                "unique_together": {("Reg_ID", "Course", "Staff")},
            },
        ),
    ]
