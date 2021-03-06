# Generated by Django 2.2 on 2019-04-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    max_length=255,
                    verbose_name='Project name'
                )),
                ('url', models.URLField(verbose_name='Project URL')),
                ('is_fork', models.BooleanField(
                    default=False,
                    verbose_name='This project is a fork'
                )),
                ('parent_url', models.URLField(
                    verbose_name='When fork, parents URL'
                )),
                ('is_visible', models.BooleanField(
                    default=False,
                    verbose_name='This project is visible'
                )),
                ('description', models.TextField()),
                ('release_url', models.URLField(verbose_name='Releases URL')),
            ],
        ),
    ]
