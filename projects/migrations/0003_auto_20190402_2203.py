# Generated by Django 2.2 on 2019-04-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190402_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='parent_url',
            field=models.URLField(
                blank=True,
                null=True,
                verbose_name='When fork, parents URL'
            ),
        ),
    ]
