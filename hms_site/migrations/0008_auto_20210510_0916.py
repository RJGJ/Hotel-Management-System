# Generated by Django 3.2.2 on 2021-05-10 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms_site', '0007_alter_reservation_custumer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='target_date',
            new_name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='custumer',
        ),
    ]