# Generated by Django 4.1.1 on 2022-10-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRole',
            fields=[
                ('Job_Role_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Job_Role_Desc', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Job_Role',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('Skill_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Skill_Name', models.CharField(max_length=50)),
                ('Skill_Desc', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Skill',
            },
        ),
        migrations.RenameModel(
            old_name='Role',
            new_name='User_Role',
        ),
        migrations.AlterModelOptions(
            name='user_role',
            options={'verbose_name': 'User_Role'},
        ),
        migrations.RenameField(
            model_name='user_role',
            old_name='Role_ID',
            new_name='User_Role_ID',
        ),
        migrations.RenameField(
            model_name='user_role',
            old_name='Role_Name',
            new_name='User_Role_Name',
        ),
    ]