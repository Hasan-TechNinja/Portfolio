# Generated by Django 5.1 on 2024-09-01 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
