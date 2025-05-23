# Generated by Django 5.1.6 on 2025-03-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_resource_is_public_room_access_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='access_level',
            field=models.CharField(choices=[('public', 'Public Access'), ('trusted', 'Trusted Access'), ('restricted', 'Restricted Access')], default='public', max_length=50),
        )
    ]
