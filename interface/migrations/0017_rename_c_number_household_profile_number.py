# Generated by Django 4.1.3 on 2023-12-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0016_alter_household_profile_c_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='household_profile',
            old_name='c_number',
            new_name='number',
        ),
    ]
