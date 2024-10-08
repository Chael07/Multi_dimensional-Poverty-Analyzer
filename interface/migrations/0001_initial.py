# Generated by Django 4.1.3 on 2024-05-04 18:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backup_Household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('indi1', models.FloatField()),
                ('indi2', models.FloatField()),
                ('indi3', models.FloatField()),
                ('indi4', models.FloatField()),
                ('indi5', models.FloatField()),
                ('indi6', models.FloatField()),
                ('indi7', models.FloatField()),
                ('indi8', models.FloatField()),
                ('indi9', models.FloatField()),
                ('indi10', models.FloatField()),
                ('indi11', models.FloatField()),
                ('indi12', models.FloatField()),
                ('indi13', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Backup_HouseholdProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('relationship', models.CharField(max_length=255)),
                ('user_number', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=255)),
                ('user_email', models.CharField(max_length=50, validators=[django.core.validators.MaxValueValidator(99999999999)])),
            ],
        ),
        migrations.CreateModel(
            name='Backup_result_classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('svm_result', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Backup_ResultMPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('mpi', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_admin', models.CharField(max_length=255)),
                ('issue', models.EmailField(max_length=254)),
                ('messages', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('indi1', models.FloatField()),
                ('indi2', models.FloatField()),
                ('indi3', models.FloatField()),
                ('indi4', models.FloatField()),
                ('indi5', models.FloatField()),
                ('indi6', models.FloatField()),
                ('indi7', models.FloatField()),
                ('indi8', models.FloatField()),
                ('indi9', models.FloatField()),
                ('indi10', models.FloatField()),
                ('indi11', models.FloatField()),
                ('indi12', models.FloatField()),
                ('indi13', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('relationship', models.CharField(max_length=255)),
                ('user_number', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=255)),
                ('user_email', models.CharField(max_length=50, validators=[django.core.validators.MaxValueValidator(99999999999)])),
            ],
        ),
        migrations.CreateModel(
            name='result_classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('svm_result', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ResultMPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('mpi', models.FloatField(default=0.0)),
            ],
        ),
    ]
