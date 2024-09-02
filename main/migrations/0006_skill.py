# Generated by Django 5.1 on 2024-09-02 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programming_languages', models.CharField(blank=True, max_length=500, null=True)),
                ('frameworks', models.CharField(blank=True, max_length=500, null=True)),
                ('tolse_and_platforms', models.CharField(blank=True, max_length=500, null=True)),
                ('databases', models.CharField(blank=True, max_length=500, null=True)),
                ('cloud_and_devops', models.CharField(blank=True, max_length=500, null=True)),
                ('soft_skills', models.CharField(blank=True, max_length=500, null=True)),
                ('operating_systems', models.CharField(blank=True, max_length=500, null=True)),
                ('version_control', models.CharField(blank=True, max_length=500, null=True)),
                ('testing', models.CharField(blank=True, max_length=500, null=True)),
                ('others', models.CharField(blank=True, max_length=900, null=True)),
            ],
        ),
    ]