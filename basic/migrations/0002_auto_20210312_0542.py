# Generated by Django 3.1.7 on 2021-03-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
