# Generated by Django 5.1 on 2024-09-02 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_skillimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]