# Generated by Django 3.1.2 on 2020-10-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMAG_APP', '0011_auto_20201008_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
