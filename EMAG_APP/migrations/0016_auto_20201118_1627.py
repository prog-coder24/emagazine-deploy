# Generated by Django 3.1.2 on 2020-11-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMAG_APP', '0015_auto_20201118_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dept_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='achievement_banner',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='achievement_field',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_banner',
            field=models.ImageField(upload_to=''),
        ),
    ]
