# Generated by Django 5.0.4 on 2024-04-27 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpreferences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreference',
            name='currency',
            field=models.CharField(default='INR - Indian Rupee', max_length=255),
        ),
    ]
