# Generated by Django 5.1 on 2024-09-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_about_email_about_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company_website',
            field=models.CharField(default='#', max_length=500),
        ),
    ]
